# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-dict-nightly
_pkgbase=${pkgbase%-dict-nightly}
pkgname=(rime-wanxiang-dict-nightly rime-wanxiang-pro-dict-nightly)
pkgver=11.0.0+r20250815.233034
_schema_version=${pkgver%%+*}
pkgrel=1
pkgdesc="万象词库——每日构建版"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${_schema_version}.tar.gz"
        build.sh)
b2sums=('8ef4eed470d32b53e2f3b935145695827ec71164d9ebe1ce22488ed3d764795b7e20248696b17abaa8effecdca6b29e9938aab368bbcc60fd29d7f2a70d3c77a'
        'ffbab0a401f81e8f520304ec8016dfb5188b84b5a948582409d25b890c75f65ad738379a01999f8315b9b73a58163f1c44feb09d51c25ef300a53bd55456395d'
        'eba4be440716431ca7eeae8a7df137f07379152b1c12563cd98e9a346d99ba29ebe11aea31285227d197e459714a6169f1dded8ff438425479ed9bbdcc7890e6'
        '36e689ea130bb77ada761d998ce6d59ab49a66a060ecfbf4560a371e0504fd415f0eba2f55d064e4f780c8341d25f788a8ec3d7cc43d339d1cce3ede966ec414'
        'e2914759365943c7947e6611f9fec1fa3c2513a3a0ea3bd6cc34661663554b39c77ac8a07eb20e942a697fc47fe7eaf83ac1594cb26d93ecb451756eec9156cc'
        '0067695cc042dfaadd98165cd3f221b395484965dd8c287f813a67e3fde8ac8997c32d2a92f5fd86214126996b75254951979bff1b20a2cd1e8ac097ae5335a0'
        'f6a2a4e7ada6c7aa5101612eb9721b55e889c707955d8a831eadbc37a03435e71b126a336aafa7f72b8b1f66912bd6b8adfafcd6f87e966a8efa9683fa4a1fcc'
        'db3308a0c6ff041a908f11a3a92c83eff94af71c91c80627b1cece19a63a79e5818b07928301454be2ff4b161c6f344423a51b832e5ec19c3c75a5028eec2ab0'
        'cf73fb8572e0a475ca26943233720299fe05ca04f5ec84607fc57796f7807d2c909b1036528977127f84d801c18b7624fef30dde2eddc669662de0296ca22023')
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
