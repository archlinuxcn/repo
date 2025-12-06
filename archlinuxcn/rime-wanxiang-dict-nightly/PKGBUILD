# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-dict-nightly
_pkgbase=${pkgbase%-dict-nightly}
pkgname=(rime-wanxiang-dict-nightly rime-wanxiang-pro-dict-nightly)
pkgver=13.7.1+r20251206.234546
_schema_version=${pkgver%%+*}
pkgrel=1
pkgdesc="万象词库——每日构建版"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${_schema_version}.tar.gz"
        build.sh)
b2sums=('15027cbf30f34e97789fc0af8b286a14aa7616a14e64251adff8feadb0cf093f44f5315dd64327568505db3b683a52db709875d36dbb73ec3cf8f88ecda0a4be'
        'e1c0a4adf4a6175ac1343c9d94d5deb6d3e134b5258111849cc714893bb1fb70d308ffb900969e510087c59489318678a3e4ad88c8a134f03d90722a1202a672'
        '9b002bd3cd2731e1bdb852e2ae6f7fbbbabdab34ed73c260b8f9848648840e8a83a8131089d874918ffb8e40e6dd1c4dd169d72b5b31411465969b7d669eb087'
        '1ffa1964dac3d5a5e4002405c66e3f83b5be773a6a129b878366d35889365e1c7f71036c5b8e37e026e3ff5bdcc51131623912c0d35824ab77c39317c71baba6'
        'd4cf0a610262b0c04af4bc36f79175351159db9f905cdc3452ef72f4dd3811e7fa0326fc5469c2660ac3cda4d85412ea369969e1be0e07227165985f40484716'
        '243a10a5bdd681c6c4e845492d1fed05f470a537cb5bda44609ca5517f33896ad0cf6cb906483b6d72f1578ccde14e1df7d3ac24d30bb649b9cecff112fdc146'
        'd7cff9f02d2dc1cc18129cc1d378321586b71ec0e0ac9ebb34704383e094659bd299b6cbb4e780e1eea9ca5939f7a878692ef933f43d23a8b8ac2b4ba6183c4d'
        '1007f468d8c6eb4196ff9d43940e843a568398275e458bb8cfabd23050fc5ef752e2e7db3ff01a7d5b3fd19f5e3d25fdf232adc08c4a95cae2836b139fcbc7e9'
        '3489fa5e94422fbef8d45097d2fa8329448a5dfc87bcfd0713a77fa6a950482f1f6d4046549f43f3952af8b4553baba04fb75f501fb3bf0dd138fe0c183f68e1'
        'fcd602555089a10ad0951e9fa94e9ff7e24da124afa8beafae6f603a3ca863ca0bccb29ccda6602a58a2ac0fb011a3778f43efb2d7abe3a3ff55de2a53f99f3a')
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
  [shouyou]="pro-shouyou-fuzhu-dicts.zip"
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
  [shouyou]="首右"
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
