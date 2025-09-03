# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-dict-nightly
_pkgbase=${pkgbase%-dict-nightly}
pkgname=(rime-wanxiang-dict-nightly rime-wanxiang-pro-dict-nightly)
pkgver=11.4.1+r20250903.114952
_schema_version=${pkgver%%+*}
pkgrel=1
pkgdesc="万象词库——每日构建版"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${_schema_version}.tar.gz"
        build.sh)
b2sums=('f68d723012e1ca6c91943fc836c524fd094ebebb85b82eb5aae3594f63ed4ccd7b96e20d79b1912805b12c9a4ebd55e30933ea8e435a795de6e21add09a74898'
        'ffbab0a401f81e8f520304ec8016dfb5188b84b5a948582409d25b890c75f65ad738379a01999f8315b9b73a58163f1c44feb09d51c25ef300a53bd55456395d'
        'dc6c5ca2f8ac87970a11cfd4f7818aa6367447ace271b33d24bc9755363c72e20ba1c8665c999e4b15ffb18200344a4bb690affcd5ad5b59d9a37e882e2cb2a0'
        '3b28ee85f21641c5426e9174b3beff22849590dc352178cd644ae57701d72069608ba639ff8cf74fc18ea18244225b6566619180149f891dbd2fb2b10be115bf'
        '4a1a765fd3364946584d5dcd264a98f4e5c00718aead666a74322484dca0de10daa3d12f4542e5a0e7330e7c01a0a4a51e263127d0977ff04e6ee6dd7af68df1'
        'f34ee64c4c8c305b6bf57cfbbc28c1103db35729569a2ebd1e34e3fee399b417921399a92f6be0e724d5f0bc6f57ee41a408825ddb47004cca2834131b7f0444'
        '01b1e3705280accc6467dd340b6d4f16c8500ffdbf8d6742ba2ef5d542decab4986f92278ee4d8813f89265bbe46b95068e804f9620e4f9ec448d6e8450bba2e'
        '74b4889e382b2927ad20422d25f541b115dff07715bd18fae7c23f7b09ddd70eb965c8dcb3db14100bbcdc8d386340f6992cf33a3e6d51b4cc64330625c9b66c'
        'e15d9fbfc8b7d30d1a84bf09eb4ac652a6cab53e6c194037737b29ff881b369cc5d3d48694b527bab19d8fedabe3a1166b11bedef847d755ab8d71ef38c647b2')
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
