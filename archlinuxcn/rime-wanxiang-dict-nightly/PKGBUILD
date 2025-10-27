# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-dict-nightly
_pkgbase=${pkgbase%-dict-nightly}
pkgname=(rime-wanxiang-dict-nightly rime-wanxiang-pro-dict-nightly)
pkgver=13.1.11+r20251028.000607
_schema_version=${pkgver%%+*}
pkgrel=1
pkgdesc="万象词库——每日构建版"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${_schema_version}.tar.gz"
        build.sh)
b2sums=('8c28ee32f26f6d47b07f4f7832c2e373e2630cc32be955e9c7e2aee94003029a86940e3e70c2d89ee904b6d389ae83a72db10e208c875e97ba23677d311fe20d'
        'e1c0a4adf4a6175ac1343c9d94d5deb6d3e134b5258111849cc714893bb1fb70d308ffb900969e510087c59489318678a3e4ad88c8a134f03d90722a1202a672'
        'bde4d05a5185c0d82ce6e206c1804d5058005f23485cbe6cdd75825e4a4011985db237148f1cea9b6db17e321f6d2dc6c88a15e8128a64121d578c226ad8585c'
        '16736d1879ce3b4e442f02d3b2df64102ee160f2ed375e1a9a00f5e6c608c486e02234fb7c0c8889c129c01d20319b58263d72a854aadf6ae9e35c19473824b9'
        '645501f8d3a2dca72ef02899f0576decc49329330c9f80136e89a1c25b1fa76f2ca41059cd1a57140ff7a56dd1cbc0703de999609672c9a5aa7d2d8927cf9786'
        '9a54de48f908c61ef92b3e19279ff9682f686849ab72d2b8bb4aa51cd79e654582922ae788d734414dd30b3370e04276e525338aa9c830744de20acc40f42022'
        'b8bb39a711a63b4b8d5b564b8824916830339252b765e98bc01df895449c1051331c466bfde663b9c2e3bfa296ef451ff87a41a4c397b0aea05c73d49853ce2a'
        'd70aab7882274b226f9ce11656c9df842ea9f6ffbef3df648e10d855d1bc24c5ac47639e42f2b45af180995af7c38759311259de16eafcabfd14572a3a268ba0'
        '4e5accb427ba064158ded4505ec11533c88fc1ae4aeddaba03c59c7cbf7d71d28553b9dec07a475e9862ec8e0a76c3f1b580da5f6c44d6e2b195a3f4af2209aa')
noextract=()
makedepends=("librime" "rime-prelude" "rime-essay" "sed" "python" "zip" "rsync")

declare -A _dict_filenames=(
  [base]="base-dicts.zip"
  [flypy]="pro-flypy-fuzhu-dicts.zip"
  [hanxin]="pro-hanxin-fuzhu-dicts.zip"
  [moqi]="pro-moqi-fuzhu-dicts.zip"
  [tiger]="pro-tiger-fuzhu-dicts.zip"
  [wubi]="pro-wubi-fuzhu-dicts.zip"
  [zrm]="pro-zrm-fuzhu-dicts.zip"
)

for _dict in "${!_dict_filenames[@]}"; do
    _filename="${_dict_filenames[${_dict}]}"
    _dict_url="${url}/releases/download/dict-nightly/${_filename}"
    source+=("${_dict_url}")
    noextract+=("${_dict_url##*/}")
done

# 拼写方案
declare -A _schemas=(
    # 注释掉的为方案支持不完善
    [flypy]="小鹤双拼"
    [mspy]="微软双拼"
    [zrm]="自然码"
    [sogou]="搜狗双拼"
    [abc]="智能ABC"
    [ziguang]="紫光双拼"
    # [pyjj]="拼音加加"
    # [gbpy]="国标双拼"
    # [lxsq]="乱序17"
    # [zrlong]="自然龙"
    # [hxlong]="汉心龙"
    [pinyin]="全拼"
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
        local tmp_dir
        tmp_dir="${srcdir}"/$(basename "$zip_file" | sed -E "s/pro-//; s/\.zip//;")
        rm -rf "$tmp_dir"
        bsdunzip -qj "$zip_file" -d "${tmp_dir}"
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
