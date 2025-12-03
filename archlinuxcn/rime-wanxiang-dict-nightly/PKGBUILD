# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-dict-nightly
_pkgbase=${pkgbase%-dict-nightly}
pkgname=(rime-wanxiang-dict-nightly rime-wanxiang-pro-dict-nightly)
pkgver=13.6.4+r20251204.003436
_schema_version=${pkgver%%+*}
pkgrel=1
pkgdesc="万象词库——每日构建版"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${_schema_version}.tar.gz"
        build.sh)
b2sums=('0864e1496aef4bcc94102a6e3a09fb803091108634b280dd1a8c68dc9b1bf6ed5c0e1d86b9fd5dc592c7da37fb15324bdca572525c50bc236a62aa676d8b11e8'
        'e1c0a4adf4a6175ac1343c9d94d5deb6d3e134b5258111849cc714893bb1fb70d308ffb900969e510087c59489318678a3e4ad88c8a134f03d90722a1202a672'
        '7a8d6efba96e118ceef26db404800690d8a1002534e2e0e5b7e7ee059ad370f252f476026ee78040d36fd17245293dc8bd7105b564d22f4f1ca524e9769bbe77'
        'cb4625cb54a6e3f5bf64148e661cca8f2bb0989277cd6cd84e6ea30b7b1d86c9713b29ac9a555ede05915d662110beb6e957dd93f33fdaa506780744c0d845f3'
        '97bde34cb52fb942b7fcf9f033fe440e82ffda68ac494c353a00cd2f31a0515b102691de9da20b60149f9b83a29c86cbcd6857ce6396b9c4c86aa4792f5541b8'
        '3fc910b37d1fa3a2b07886b118646f572b1914c7e9b83b47ebc09c72dc48ff8a39ede9403f0ce2e75ab8ec877672452b2a6d38fdeb8181e3c3f1a0567ced19f8'
        '55984c48ae599156613965d0fbfc30943887affcd11cb2c0fc6ba83e765f999c2a2ea6a15ea4f1af028db185792b1acef07c27c43414755d4cf9459ca610345d'
        '4ebb03dc6a78e2d7cb4741b1b3e6980889770e8ffc5653907f4d865801ef1b5f6f1ef2a0cb473224e98f9e76a324dbe92db6f829971cf337359f308723dbcabc'
        '0a494cbfa411ada80c6b182c67f7ae955b8cf5c41b30b6e76f61dcae027bde46672146fa1b61533088cead0888bec955297aa77675ce8754225a81294260fa05'
        '7687a095b6ab2f2672a0f26c864533aa6ac7cf1723a2a9772067f1dcb66ccf9c7636409b39fc8872d6dab6c93f980c652aa52859083ca47458f96b30f498fc24')
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
