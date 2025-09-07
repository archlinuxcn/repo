# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-dict-nightly
_pkgbase=${pkgbase%-dict-nightly}
pkgname=(rime-wanxiang-dict-nightly rime-wanxiang-pro-dict-nightly)
pkgver=12.0.3+r20250907.211655
_schema_version=${pkgver%%+*}
pkgrel=1
pkgdesc="万象词库——每日构建版"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${_schema_version}.tar.gz"
        build.sh)
b2sums=('93be785c1653e1106611fb1a6c6706ce5f2622db19781dd5670ece15af9ea7def35d75e42e68a42fbc5d5a471971148619ff47f918f2b7066ba69e851a0d0f08'
        'ffbab0a401f81e8f520304ec8016dfb5188b84b5a948582409d25b890c75f65ad738379a01999f8315b9b73a58163f1c44feb09d51c25ef300a53bd55456395d'
        '0273cbf0c3a6834284a3990ece6c4c8538102bad1a408a9d41319b50ce27dd54cfaf69413862d64953a6fcc69beddd23516c7f9327f0d54f2ab9b1f8499d631f'
        '7b29b28c1a8514c0d94470becd78958ae3b5a05847731dfbf2a69f8636a9c3a7b7f5c6ac9ffbe27f0ac732277780f10d7438a480ab63a035044cb7e3250c4221'
        'b87f1cfc843a6fbbbf618277e08c7e7bf57e726791ea523bddf6b244d6d1a048de99c5b63bb7e2a13e1a32a4bd5b126bb0f80a3909998688243e4cd2ea110a54'
        '44448ba04511f6829483eb7c4c040cef4304a80fae94b67c6a82d313c2db761d0fdca72c19a6644f7bdb0bae817567f93e48957df089ae705dad484624fec79b'
        'c4fc6aca14125efb1c343e3268463e1d2870fba11268b0725a61828514dcec61a84a0ac346d86a0ba68eaa6526f0183af4e611da073b20bb66db92c8d80024be'
        'e7c2c17fc835d7cbf449f3b24488daf9ae5a4016f09cd743afd25d2940445b1611871e28bdd1a0182dd1057bc29f3f67b40e0c8e2ecb663caa7d2dd7f546c4c2'
        'ffa884d911e70e07ac72a39aae6a8f342aab3cf6ba42333c122fe5ba8a9f137f73ce2b8d29d3f5b8a7277c2d141c17abae5753d37a5c816800c0b3e641c64067')
noextract=()
makedepends=("librime" "rime-prelude" "rime-essay" "sed" "python" "zip")

declare -A _dict_filenames=(
  [moqi]="1-pro-moqi-fuzhu-dicts.zip"
  [flypy]="2-pro-flypy-fuzhu-dicts.zip"
  [zrm]="3-pro-zrm-fuzhu-dicts.zip"
  [tiger]="4-pro-tiger-fuzhu-dicts.zip"
  [wubi]="5-pro-wubi-fuzhu-dicts.zip"
  [hanxin]="6-pro-hanxin-fuzhu-dicts.zip"
  [base]="8-base-dicts.zip"
)

for _dict in "${!_dict_filenames[@]}"; do
    _filename="${_dict_filenames[${_dict}]}"
    _dict_url="${url}/releases/download/dict-nightly/${_filename}"
    source+=("${_dict_url}")
    noextract+=("${_dict_url##*/}")
done

# 拼写方案
declare -A _schemas=(
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

# 辅助码类型
declare -A _fuzhus=(
  [zrm]="自然码"
  [moqi]="墨奇"
  [flypy]="小鹤"
  [hanxin]="汉心"
  [wubi]="五笔前2"
  [tiger]="虎码首末"
)

build() {
    cd "${srcdir}/rime_wanxiang-${_schema_version}" || exit 1

    msg2 "release building..."
    bash .github/workflows/scripts/release-build.sh >/dev/null

    msg2 "updating dicts..."
    for zip_file in "${srcdir}"/*.zip; do
        local tmp_dir && tmp_dir="${srcdir}/$(basename "${zip_file%%.zip}")" && rm -rf "$tmp_dir"
        bsdunzip -q "$zip_file" -d "${tmp_dir}"
        (
            local target_dir
            target_dir="${srcdir}"/$(basename "$zip_file" | sed -E "s/.*-(base-dicts|\w+-fuzhu-dicts).*/\1/")
            rm -rf "$target_dir" && mkdir "${target_dir}"

            cd "${tmp_dir}" || exit 1
            if [[ $(find . -mindepth 1 -maxdepth 1 | wc -l) -eq 1 ]]; then
                find . -mindepth 2 -type f -exec sh -c '
                    src="$1"
                    dest="$2/${src#./*/}"
                    install -Dm664 "$src" "$dest"
                ' sh {} "$target_dir" \;
            else
                find . -mindepth 1 -type f -exec install -Dm664 {} "${target_dir}/{}" \;
            fi
        )
        rm -rf "${tmp_dir}"
    done

    local _dir && for _dir in dist/*; do
        [[ ! -d $_dir ]] && continue
        (
            local target_dir && target_dir=$(realpath "$_dir"/dicts) && rm -rf "${target_dir:?}"/*
            local fuzhu_type && fuzhu_type=$(basename "$_dir" | sed "s/rime-wanxiang-//")

            cd "${srcdir}/${fuzhu_type}-dicts" || exit 1
            find . -mindepth 1 -type f -exec install -Dm664 {} "$target_dir"/{} \;
        )
    done

    msg2 "schema building..."
    bash "${srcdir}"/build.sh
}

_package() {
    dist_dir=${1//rime-wanxiang-} && dist_dir=${dist_dir//-nightly}
    cd "${srcdir}/dist/${dist_dir}" || exit 1
    find . -type f -exec install -Dm664 {} "${pkgdir}"/usr/share/rime-data/{} \;
}

package_rime-wanxiang-dict-nightly() {
    pkgdesc="万象拼音词库基础数据——每日构建版"
    provides=("${_pkgbase}-dict=${_schema_version}")
    conflicts=("$_pkgbase-dict")
    replaces=("${_pkgbase}-dict-zh-nightly")
    # shellcheck disable=SC2128
    _package "$pkgname"
}
package_rime-wanxiang-pro-dict-nightly() {
    pkgdesc="万象拼音双拼辅助码版词库基础数据——每日构建版"
    conflicts=("$_pkgbase-dict" "$_pkgbase-dict-nightly" "$_pkgbase-pro-dict")
    provides=("${_pkgbase}-pro-dict=${_schema_version}")
    replaces=("${_pkgbase}-pro-dict-zh-nightly")
    # shellcheck disable=SC2128
    _package "$pkgname"
}

#
# ${_pkgbase}-<schema>
# - ${_pkgbase}-data
# - ${_pkgbase}-dict-<schema>
#   - ${_pkgbase}-dict
# 
# ${_pkgbase}-pro-<schema>
# - ${_pkgbase}-pro-data
# - [${_pkgbase}-pro-data-fuzhu]
#   - ${_pkgbase}-pro-data-<fuzhu>-fuzhu
#     - ${_pkgbase}-pro-dict-<fuzhu>-fuzhu
#       - ${_pkgbase}-pro-dict
# 
for _schema in "${!_schemas[@]}"; do
    _schema_name=${_schemas[$_schema]}

    # 基础版词库
    _pkgname=${_pkgbase}-dict-${_schema}-nightly && pkgname+=("${_pkgname}")
    _conflicts=()
    for _schema_c in "${!_schemas[@]}"; do
        _conflicts+=("${_pkgbase}-dict-${_schema_c}")
        [[ "${_schema_c}" == "${_schema}" ]] && continue
        _conflicts+=("${_pkgbase}-dict-${_schema_c}-nightly")
    done
    eval "package_${_pkgname}() {
        pkgdesc='万象拼音标准版词库——每日构建版（${_schema_name}方案）'
        depends=('${_pkgbase}-dict-nightly')
        conflicts=(${_conflicts[*]})
        provides=('${_pkgbase}-dict-${_schema}=${_schema_version}')
        _package ${_pkgname}
    }"
done

for _fuzhu in "${!_fuzhus[@]}"; do
    _fuzhu_name=${_fuzhus[$_fuzhu]}

    # PRO 版词库
    _pkgname=${_pkgbase}-pro-dict-${_fuzhu}-fuzhu-nightly && pkgname+=("${_pkgname}")
    _conflicts=()
    for _fuzhu_c in "${!_fuzhus[@]}"; do
        _conflicts+=("${_pkgbase}-dict-${_fuzhu_c}")
        [[ "${_fuzhu_c}" == "${_schema}" ]] && continue
        _conflicts+=("${_pkgbase}-dict-${_fuzhu_c}-nightly")
    done
    eval "package_${_pkgname}() {
        pkgdesc='万象拼音双拼辅助码词库——每日构建版（${_fuzhu_name}辅助）'
        depends=('${_pkgbase}-pro-dict-nightly')
        conflicts=(${_conflicts[*]})
        provides=('${_pkgbase}-pro-dict-${_fuzhu}-fuzhu=${_schema_version}')
        _package ${_pkgname}
    }"
done
