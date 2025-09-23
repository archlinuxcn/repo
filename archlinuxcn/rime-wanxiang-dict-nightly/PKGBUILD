# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-dict-nightly
_pkgbase=${pkgbase%-dict-nightly}
pkgname=(rime-wanxiang-dict-nightly rime-wanxiang-pro-dict-nightly)
pkgver=12.6.6+r20250923.161654
_schema_version=${pkgver%%+*}
pkgrel=1
pkgdesc="万象词库——每日构建版"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${_schema_version}.tar.gz"
        build.sh)
b2sums=('f1f18e027fbe65a7432183447bbd69f7ea9e07ce7e5496c4277d6d6133b7e952a97a2f10d28a21a82a87cb9179204afb1abcc92cec767a718db235b87f04bcca'
        'ffbab0a401f81e8f520304ec8016dfb5188b84b5a948582409d25b890c75f65ad738379a01999f8315b9b73a58163f1c44feb09d51c25ef300a53bd55456395d'
        '074b59298fae417a40abe86c89fda1fe853a8d0aaf442da6ed0c8501f80b638ad6527e7db9eba852b0d3a141a298b9c393c4599a885db94ae06e88cadfb25ce5'
        '0e581936eeaad9019f0bd69a588c718f0b110603ec819ddbc7848e6d167d7f04b20b7c0f0c263147664f006911313b065e3037738dae6c1a1276c450608f1435'
        'ef4e77c57478d8716fbaf0f96898748247e3220cb4f8f981e5e954e461be50a060c2b0293bd26540381c232d1058662ca649d47a5055e5a678e1cf1a34f44d7e'
        '9c43cf2bb302b749ee3d538d298188ff7bdf0b3af0535f1334d4144c9e2546ca67e4f322c82fe8a754ebe83712b7f95e768e125848a3b7372f2c85e71228da6a'
        '9967d37e104da020f283cf98aaa3e3fda799ee450fe12ffde9ace2b741af914af3359d4c79bd898953d6b6a823531db1e6365fc9d754b56523428338b72db296'
        '47f8bc56fefd1d04fa5f1f071e98c51332457e945d0ac3d3ac6ab41f7b7ee8efd6f96df9a1ac14eb604d2c2ec2fdb747ef34eb1e6dadc28117329338a83b1333'
        '98d47927d373564a75df775c7f9de7b8af1dfec17ac8458b7ace6839ee4a0ca4d0ead73d509375b4d3e44b8d96c7cb70d7c89065de34de75dfb750234d4571ea')
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
