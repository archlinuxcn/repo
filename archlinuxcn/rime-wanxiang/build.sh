#!/bin/bash
set -e

# 拼写方案
declare -A schemas=(
    [pinyin]="全拼"
    [zrm]="自然码"
    [flypy]="小鹤双拼"
    [mspy]="微软双拼"
    [sogou]="搜狗双拼"
    [abc]="智能ABC"
    [ziguang]="紫光双拼"
    # 以下方案支持不完善
    # [pyjj]="拼音加加"
    # [gbpy]="国标双拼"
    # [lxsq]="乱序17"
    # [hanxin]="汉心龙"
    # [zrlong]="自然龙"
)

src_dir=$(realpath "$PWD"/../)
dist_dir=$(realpath "${src_dir}"/dist)
rm -rf "${dist_dir}"
release_dist_dir=$(realpath "./dist/")

build_dicts() {
    for _f in $(pacman -Qql rime-prelude rime-essay | grep -Ev "(/|default.yaml)$"); do ln -sf "${_f}" .; done
    for _s in "$@"; do rime_deployer --compile "${_s}"; done
    find . -type l -delete
}

extract_dicts() {
    local schema_type=$1 # pro | base
    local schema=$2      # zrm | pinyin | ...
    local fuzhu_type=$3  # zrm-fuzhu | ...
    local clean=$4

    local target_dir
    target_dir=${dist_dir}/dict-${schema} &&
        [[ "$schema_type" == "pro" ]] && target_dir=${dist_dir}/pro-dict-${schema}-"${fuzhu_type}"

    echo "-> build $(basename "${target_dir}")..."

    find ./dicts -mindepth 1 -type f -exec install -Dm664 {} "${target_dir}"/{} \;

    grep -rl "\sdicts/" ./*.dict.yaml | while read -r dict_file; do
        dict_name=$(sed -n 's/.*name: \([^ ]*\)/\1/p' ./"${dict_file}")
        install -Dm664 ./build/"${dict_name}".*.bin -t "${target_dir}"/build
    done

    if [[ -n "$clean" ]]; then
        rm -rf ./dicts ./build
    fi
}

build_schema() {
    local schema_type=$1 # pro | base
    local schema=$2      # pinyin | ...
    local algebra=$3     # 拼音 | ...
    local fuzhu_type=$4  # zrm-fuzhu | ...

    # 更新拼写方案
    sed -Ei \
        -e "/^set_shuru_schema:/,/^[^[:space:]]/ { s|^(\s+__include:\s*)\S+(\s*.*)|\1${algebra}\2| }" \
        wanxiang*.schema.yaml

    build_dicts wanxiang*.schema.yaml

    extract_dicts "${schema_type}" "${schema}" "${fuzhu_type}" true

    # 预设处理
    local suggestion="suggestion" && [[ ${schema_type} == "pro" ]] && suggestion="pro_suggestion"
    mv default.yaml ./wanxiang_${suggestion}.yaml
}

get_shuru_schema() {
    local name
    name=$(sed -n '/set_shuru_schema:/,/^[^ ]/{/__include:/{s/^[ \t]*__include:[ \t]*//;s/[ \t]*#.*$//;s/[ \t]*$//;p}}' "$1")
    for schema in "${!schemas[@]}"; do
        local algebra="${schemas[$schema]}"
        if [[ "$algebra" == "$name" ]]; then
            echo "$schema"
            break
            return
        fi
    done

    exit 1
}

build_dist_dir() {
    local release_dir=$1
    local fuzhu_type=${release_dir##*rime-wanxiang-}
    local schema_type=pro && [[ $fuzhu_type == "base" ]] && schema_type="base"

    # 预编译词典，降低后续的编译时间
    echo "-> prebuild $fuzhu_type"
    pushd "$release_dir" >/dev/null &&
        build_dicts wanxiang*.schema.yaml &&
        popd >/dev/null

    local temp_dir="${src_dir}"/tmp/"${fuzhu_type}"
    mkdir -p "${src_dir}"/tmp
    rm -rf "${temp_dir}"
    cp -r "${release_dir}" "${temp_dir}"

    # 构建方案
    pushd "$temp_dir" >/dev/null &&
        # 处理基础版和辅码版方案
        for schema in "${!schemas[@]}"; do
            # pro 基于自然码辅助生成，且遵循上游，不生成全拼方案
            if [[ "${schema_type}" == "pro" ]]; then
                [[ ${schema} == "pinyin" ]] && continue
                # [[ ${fuzhu_type} != "zrm-fuzhu" ]] && [[ ${fuzhu_type} != "flypy-fuzhu" ]] && continue
            fi

            local pkg_schema="${schema}" && [[ "${schema_type}" == "pro" ]] && pkg_schema="pro-${schema}-${fuzhu_type}"

            local target_dir="${dist_dir}/${pkg_schema}"

            find . -type f ! \( \
                -path "./custom/*" -o \
                -path "./lua/librime.lua" -o \
                -path "./lua/tips/tips_user.*" -o \
                -path "./custom_phrase.txt" -o \
                -path "./squirrel.yaml" -o \
                -path "./weasel.yaml" -o \
                -path "./*.trime.yaml" -o \
                -path "./*.md" -o \
                -path "./version.txt" \
                \) \
                -exec install -Dm664 {} "${target_dir}"/{} \;

            local algebra="${schemas[$schema]}"
            echo "-> build $(basename "${target_dir}")..."
            pushd "$target_dir" >/dev/null &&
                build_schema $schema_type "${schema}" "${algebra}" "${fuzhu_type}" &&
                popd >/dev/null
        done &&
        popd >/dev/null
}

release_dists=()
while IFS= read -r d; do release_dists+=("$d"); done < <(find "${release_dist_dir}" -mindepth 1 -maxdepth 1 -type d)

pids=()
cleanup() {
    echo "Ctrl+C pressed. Exiting subshell."
    for pid in "${pids[@]}"; do
        kill -TERM "$pid" || true
    done
    exit 130
}
trap cleanup SIGINT

for i in "${!release_dists[@]}"; do
    build_dist_dir "${release_dists[$i]}" &
    pids+=($!)
done
wait

# 提取公共包
extract_shared_files() {
    local dist_dir1=$1
    local dist_dir2=$2
    local target_dir=$3
    local clean_type=$4

    local target_basename && target_basename=$(basename "$target_dir")
    local extract_type="data" && [[ $target_basename == *dict* ]] && extract_type="dict"

    echo "-> extract shared files: $target_basename"

    local filename && diff -rsq --no-dereference "${dist_dir1}" "${dist_dir2}" |
        grep ' are identical$' |
        sed -E "s|^Files '?${dist_dir1}/([^']+)'? and .*|\1|" |
        while IFS= read -r filename; do
            install -Dm664 "${dist_dir1}/${filename}" "${target_dir}"/"${filename}"

            if [[ -z "$clean_type" ]]; then
                rm -rf "./${dist_dir1}/${filename}" "./${dist_dir2}/${filename}"
            else
                if [[ $extract_type == "data" ]]; then
                    local schema && for schema in "${!schemas[@]}"; do
                        if [[ $target_basename == pro-* ]]; then
                            if [[ "$target_basename" == "pro-data" ]]; then
                                rm -rf ./pro-"${schema}"-*/"${filename}"
                            else
                                local fuzhu && fuzhu=$(echo "$target_basename" | sed -E "s|.*-([^-]+)-fuzhu|\1|")
                                rm -rf ./pro-"${schema}"-"${fuzhu}"-fuzhu/"${filename}"
                            fi
                        else
                            rm -rf ./"${schema}"/"${filename}"
                        fi
                    done
                elif [[ $extract_type == "dict" ]]; then
                    if [[ $target_basename == pro-* ]]; then
                        if [[ "$target_basename" == "pro-dict" ]]; then
                            rm -rf ./pro-dict-*/"${filename}"
                        else
                            local fuzhu && fuzhu=$(echo "$target_basename" | sed -E "s|.*-([^-]+)-fuzhu|\1|")
                            rm -rf ./pro-dict-*-"${fuzhu}"-fuzhu/"${filename}"
                        fi
                    else
                        rm -rf ./dict-*/"${filename}"
                    fi
                fi
            fi
        done
}

pushd "${dist_dir}" >/dev/null && (
    extract_shared_files dict-pinyin dict-zrm "${dist_dir}/dict" all
    extract_shared_files pro-dict-zrm-zrm-fuzhu pro-dict-flypy-flypy-fuzhu "${dist_dir}/pro-dict" all
    for r_dist in "${release_dists[@]}"; do
        _fuzhu=$(basename "$r_dist" | sed 's|rime-wanxiang-||')
        # 提取不同辅助码方案的共用字典文件
        [[ ${_fuzhu} == "base" ]] && continue
        extract_shared_files "pro-dict-zrm-${_fuzhu}" "pro-dict-flypy-${_fuzhu}" "${dist_dir}/pro-dict-${_fuzhu}" all
    done

    # 基础版共用数据
    extract_shared_files pinyin zrm "${dist_dir}/data" all
    # PRO版共用数据
    extract_shared_files pro-zrm-zrm-fuzhu pro-flypy-flypy-fuzhu "${dist_dir}/pro-data" all
    for r_dist in "${release_dists[@]}"; do
        _fuzhu=$(basename "$r_dist" | sed 's|rime-wanxiang-||')
        # PRO 同辅助码的共用数据
        [[ ${_fuzhu} == "base" ]] && continue
        extract_shared_files pro-zrm-"${_fuzhu}" pro-flypy-"${_fuzhu}" "${dist_dir}/pro-data-${_fuzhu}" all
    done
) && popd >/dev/null
