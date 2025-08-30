# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-dict-nightly
_pkgbase=${pkgbase%-dict-nightly}
pkgname=(rime-wanxiang-dict-nightly rime-wanxiang-pro-dict-nightly)
pkgver=11.4.0+r20250830.171106
_schema_version=${pkgver%%+*}
pkgrel=1
pkgdesc="万象词库——每日构建版"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${_schema_version}.tar.gz"
        build.sh)
b2sums=('a7003bfb5576155e3ce2634439b348f3d38674534e6a3a3a57a488fa149e8c334c2f83ea248152166dd4da2747096cddd039a02187e6f27ca6c4a2d639230479'
        'ffbab0a401f81e8f520304ec8016dfb5188b84b5a948582409d25b890c75f65ad738379a01999f8315b9b73a58163f1c44feb09d51c25ef300a53bd55456395d'
        'bb7228d8d13f47f0dc271f37ce793843237e25ae67aeeedcf19ceee632facad5e8a8e272a32a70ed22aa736a2b4d03b8a585aabb22e248d049da2af853d65f1b'
        '9c37f13d142768565b0715f85bc29ef3437afadf8cb696ba65d18abd778922d4b8a4d93c724748066b1685c5aae3a29f0f8cd90f1bf950d669ed447252caf43d'
        '9f1ceca3299eb585676d3709adc44a923bd8af8fcca5e58ab416a6e5e1c45ca8dd9a3f478c9280361023956042a28ad91162c94ec7f4b602f940dd3b485ce6ac'
        'd4d666b62d10804d4d267edc5fcfee13eaa00d3f88347e22b4f268cbc6c66152c155b2a6f9059183e937e3ed48e96a880c59bd2149f63ef9d0614a512b2a9755'
        '6282a58cc4de30b632f9bd717c8a04cc9e45e5a96d4b5a479b8fb7fe646503ccb8f053d4899f3aac5a6583894355f013f5ef3af00d4aba8c576ab0aac09f89a7'
        'deeb06a011673158d175df733a102a6a6e29e852508893d161241efa18440dfb0df55ff47824a108104207a440b8cc9b69870b0de9673539f034345044557286'
        '75572d7e37651ddaded82b1a91b102862ad767c89ced35cfc2b7286f7ea54794fba4cc6d35c5f4c451deb2361d6e4ea32557785ff29c64702b4ab28058bf244f')
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
