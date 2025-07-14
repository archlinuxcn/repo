# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang
pkgname=(rime-wanxiang-data)
pkgver=8.8.0
pkgrel=1
pkgdesc="万象拼音：带声调的拼音词库，万象拼音系列方案基础版，可扩展全拼、双拼、中英混输、语言模型"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${pkgver}.zip")
b2sums=('e15cb31ec39717540c9e3955fdce0c1284a361f7466a5132bf148b9e648d27b2ae2f646af755aec12a08c79b717dd0fe8fd311da28087ccc315091c5bfa1a392')

makedepends=("librime" "rime-prelude" "rime-essay" "sed" "python" "zip")
build() {
    cd "${srcdir}/rime_wanxiang-${pkgver}" || exit 1
    bash .github/workflows/scripts/release-build.sh
}

_build_dicts() {
    for _f in $(pacman -Qql rime-prelude rime-essay | grep -v "/$"); do ln -sf "${_f}" .; done

    for _s in "$@"; do rime_deployer --compile "${_s}"; done

    find . -type l -delete
    rm -f build/*.txt
}

package_rime-wanxiang-data() {
    pkgdesc="万象拼音基础数据"
    depends=(lua librime rime-wanxiang-gram-zh-hans)
    optdepends=('libnotify: notification support in lua scripts')

    cd "${srcdir}/rime_wanxiang-${pkgver}/dist/rime-wanxiang-base" || exit 1

    find . -type f ! \( \
            -path "./custom/*" -o \
            -path "./custom_phrase.txt" -o \
            -path "./en_dicts/flypy.txt" -o \
            -path "./en_dicts/mspy.txt" -o \
            -path "./en_dicts/pinyin.txt" -o \
            -path "./en_dicts/sogou.txt" -o \
            -path "./en_dicts/zrm.txt" -o \
            -path "./jm_dicts/flypy.txt" -o \
            -path "./jm_dicts/zrm.txt" -o \
            -path "./lua/librime.lua" -o \
            -path "./lua/tips/tips_user.*" -o \
            -path "./zh_dicts/*" -o \
            -path "./zh_dicts_pro/*" -o \
            -path "./default.yaml" -o \
            -path "./squirrel.yaml" -o \
            -path "./wanxiang.*.yaml" -o \
            -path "./wanxiang_pro.*.yaml" -o \
            -path "./wanxiang_en.schema.yaml" -o \
            -path "./wanxiang_radical.*.yaml" -o \
            -path "./wanxiang_charset.*.yaml" -o \
            -path "./wanxiang_lookup.*.yaml" -o \
            -path "./weasel.yaml" -o \
            -path "./*.trime.yaml" \
        \) \
        -exec install -Dm664 {} "${pkgdir}"/usr/share/rime-data/{} \;

    pushd "${pkgdir}"/usr/share/rime-data/
        _build_dicts wanxiang*.schema.yaml
    popd
}

# base 和 pro 的主方案
declare -A _schemas=(
    [pinyin]="全拼"
    [zrm]="自然码"
    [flypy]="小鹤双拼"
    [mspy]="微软双拼"
    [sogou]="搜狗双拼"
    # 以下没有对应的英文词库
    # [hanxin]="汉心龙"
    # [..]="自然龙"
    # [..]="智能ABC"
    # [..]="紫光双拼"
    # [..]="拼音加加"
    # [..]="乱序17"
)
declare -A _fuzhu_names=(
#   [all]="全"
  [zrm]="自然码"
  [moqi]="墨奇"
  [flypy]="小鹤"
  [jdh]="简单鹤"
  [hanxin]="汉心"
  [wubi]="五笔前2"
  [tiger]="虎码首末"
)

for _schema in "${!_schemas[@]}"; do
    _name="${_schemas[${_schema}]}"

    _pkgname=${pkgbase}-${_schema}-data
    pkgname+=("${_pkgname}")
    _conflicts=()
    for _schema_c in "${!_schemas[@]}"; do
        if [[ "${_schema_c}" == "${_schema}" ]]; then continue; fi
        _conflicts+=("${pkgbase}-${_schema_c}-data")
    done
    eval "package_${_pkgname}() {
        pkgdesc='万象拼音基础数据（${_name}方案）'
        depends=(rime-wanxiang-data)
        conflicts=(${_conflicts[*]})

        _package_schema shared $_schema $_name
    }"

    _pkgname=${pkgbase}-${_schema}
    pkgname+=("${_pkgname}")
    _conflicts=()
    for _schema_c in "${!_schemas[@]}"; do
        if [[ "${_schema_c}" == "${_schema}" ]]; then continue; fi
        _conflicts+=("${pkgbase}-${_schema_c}")
    done
    eval "package_${_pkgname}() {
        pkgdesc='万象拼音标准版（${_name}方案）'
        depends=('rime-wanxiang-${_schema}-data' 'rime-wanxiang-dict-zh=${pkgver}')
        provides=('rime-wanxiang=${pkgver}')
        conflicts=(${_conflicts[*]})
        install='post.install'

        _package_schema base $_schema $_name
    }"

    # 基础版中文词库
    _pkgname=${pkgbase}-dict-zh
    if [[ " ${pkgname[*]} " != *" $_pkgname "* ]]; then
        pkgname+=("${_pkgname}")
        eval "package_${_pkgname}() {
            pkgdesc='万象拼音中文词库（标准版）'

            _package_dict_zh base
        }"
    fi

    # pro 版上游只建议使用双拼
    if [[ $_schema == "pinyin" ]]; then continue; fi

    _pkgname=${pkgbase}-pro-${_schema}
    pkgname+=("${_pkgname}")
    _conflicts=()
    for _schema_c in "${!_schemas[@]}"; do
        if [[ "${_schema_c}" == "${_schema}" ]]; then continue; fi
        _conflicts+=("${pkgbase}-pro-${_schema_c}")
    done
    eval "package_${_pkgname}() {
        pkgdesc='万象拼音双拼辅助码版（${_name}方案）'
        depends=('rime-wanxiang-${_schema}-data' 'rime-wanxiang-pro-dict-zh=${pkgver}')
        provides=('rime-wanxiang-pro=${pkgver}')
        conflicts=(${_conflicts[*]})
        install='post.install'

        _package_schema pro $_schema $_name
    }"

    # Pro 中文词库
    if [[ $_schema != "zrm" ]]; then continue; fi

    for _fuzhu in "${!_fuzhu_names[@]}"; do
        _fuzhu_name="${_fuzhu_names[${_fuzhu}]}"
        _pkgname=${pkgbase}-pro-dict-zh-${_fuzhu}
        pkgname+=("${_pkgname}")
        _conflicts=()
        for _fuzhu_c in "${!_fuzhu_names[@]}"; do
            if [[ "${_fuzhu_c}" == "${_fuzhu}" ]]; then continue; fi
            _conflicts+=("${pkgbase}-pro-dict-zh-${_fuzhu_c}")
        done
        eval "package_${_pkgname}() {
            pkgdesc='万象拼音中文词库（${_fuzhu_name}辅助码版）'
            provides=('${pkgbase}-pro-dict-zh=${pkgver}')
            conflicts=(${_conflicts[*]})

            _package_dict_zh pro $_fuzhu
        }"
    done
done

_package_schema() {
    _type=$1
    _en_dict="en_dicts/$2"
    _shuru_schema=$3

    _dist_dir="rime-wanxiang-base"
    # 所有 pro 版除字典差异外，其他均一致，这里使用 zrm 作为基础生成
    if [[ $_type == 'pro' ]]; then _dist_dir="rime-wanxiang-zrm-fuzhu"; fi
    cd "${srcdir}/rime_wanxiang-${pkgver}/dist/${_dist_dir}" || exit 1

    if [[ $_type == 'shared' ]]; then
        find . -type f \( \
            -path "./wanxiang_radical.*.yaml" -o \
            -path "./wanxiang_en.*.yaml" -o \
            -path "./en_dicts/*.dict.yaml" -o \
            -path "./${_en_dict}*" \
            \) -exec install -Dm664 {} "${pkgdir}"/usr/share/rime-data/{} \;
    else
        find . -type f \( \
            -path "./default.yaml" -o \
            -path "./wanxiang.*.yaml" -o \
            -path "./wanxiang_pro.*.yaml" -o \
            -path "./wanxiang_charset.*.yaml" -o \
            -path "./wanxiang_lookup.schema.yaml" \
            \) -exec install -Dm664 {} "${pkgdir}"/usr/share/rime-data/{} \;
    fi

    pushd "${pkgdir}"/usr/share/rime-data/
        _schema_files=()
        if [[ $_type == 'shared' ]]; then
            for _s in wanxiang_{radical,en}.schema.yaml; do
                sed -Ei \
                    -e "/^set_shuru_schema:/,/^[^[:space:]]/ { s|^(\s+__include:\s*)\S+(\s*.*)|\1${_shuru_schema}\2| }" \
                    "${_s}"
            done
            for _sf in *.schema.yaml; do
                _schema_files+=("${_sf}")
            done
        else
            _suggestion_name="wanxiang_suggestion.yaml"
            _main_schema_file=wanxiang.schema.yaml
            if [[ $_type == 'pro' ]]; then
                _suggestion_name="wanxiang_pro_suggestion.yaml"
                _main_schema_file="wanxiang_pro.schema.yaml"
            fi

            # suggestion file
            if [[ -f default.yaml ]]; then
                mv default.yaml $_suggestion_name
            fi

            # patch current schema
            sed -Ei \
                -e "/^set_shuru_schema:/,/^[^[:space:]]/ { s|^(\s+__include:\s*)\S+(\s*.*)|\1${_shuru_schema}\2| }" \
                -e "/^set_cn_en:/,/^[^[:space:]]/ { s|^(\s+user_dict:\s*)\S+(\s*.*)|\1${_en_dict}\2| }" \
                ${_main_schema_file}

            # 编译此包中的 dicts
            # wanxiang_en           因为 schema 有变更，在这里编译
            # wanxiang_lookup       每个辅码版本不一样，在辅码包中编译
            # wanxiang/wanxiang_pro 每个符码版本不一样，在辅码包中编译
            mapfile -d '' -t _schema_files < <(find . -maxdepth 1 -type f \
                -name "*.schema.yaml" \
                ! -name ${_main_schema_file} \
                ! -name "wanxiang_lookup.*" \
                -print0)
        fi

        _build_dicts "${_schema_files[@]}"

        # 已在 data 包中，这里仅用于编译
        rm -rf ./en_dicts/*.dict.yaml ./wanxiang_en.dict.yaml
    popd
}

_package_dict_zh() {
    _type=$1
    _fuzhu=$2

    _dist_dir="rime-wanxiang-base"
    if [[ $_type == 'pro' ]]; then
        _dist_dir="rime-wanxiang-${_fuzhu}-fuzhu";
    fi
    cd "${srcdir}/rime_wanxiang-${pkgver}/dist/${_dist_dir}" || exit 1

    find . -type f \( \
        -path "./zh_dicts*" -o \
        -path "./wanxiang.*.yaml" -o \
        -path "./wanxiang_pro.*.yaml" -o \
        -path "./wanxiang_lookup.*.yaml" -o \
        -path "./wanxiang_symbols.yaml" \
        \) \
        -exec install -Dm664 {} "${pkgdir}"/usr/share/rime-data/{} \;

    pushd "${pkgdir}"/usr/share/rime-data/
        _build_dicts wanxiang*.schema.yaml
        rm -f ./*.schema.yaml ./{wanxiang,wanxiang_pro}.dict.yaml ./wanxiang_symbols.yaml
    popd
}
