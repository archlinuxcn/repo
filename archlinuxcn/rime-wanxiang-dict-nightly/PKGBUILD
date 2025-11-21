# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-dict-nightly
_pkgbase=${pkgbase%-dict-nightly}
pkgname=(rime-wanxiang-dict-nightly rime-wanxiang-pro-dict-nightly)
pkgver=13.4.5+r20251121.190927
_schema_version=${pkgver%%+*}
pkgrel=1
pkgdesc="万象词库——每日构建版"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${_schema_version}.tar.gz"
        build.sh)
b2sums=('36bc5a3e4ccdb181ff595b763767d70c7671d9fd7d6a3be2abe7a05d1d5c4695656cc8534894c5aa080c38928e49d6dbc47639e1ea9e197ebde7a0fc52deeca0'
        'e1c0a4adf4a6175ac1343c9d94d5deb6d3e134b5258111849cc714893bb1fb70d308ffb900969e510087c59489318678a3e4ad88c8a134f03d90722a1202a672'
        '40115a1551cabe4d88e650dd96d003b4e3a827c4f0de56151cc292fa0ae50e9e5873c62c6379c3ba2908ef3045c290a93e3c664f0a762b376fc96d772201268a'
        '2fe3f55af3c90ace410e63b1421152b4da73fd8446c5e3d2ae7321ff20600dcd55dfa0bf7684868aad7d6f88b1aa208f4bdd0aae564439edd75b4f82eee499bc'
        'bfb0da6694cdb698e2e1ed3df352a0957db763bfab27487055de28e5a0f07a1e08339efeee248f77ccdf33fdcbe9df4633e96af5d010400ff4d854051106e1ad'
        'de34ee2f352454408eab7fe3d3d611cb55c5d14a7c041a7dd7004b44470a83e91b5a1ea1e36fbda774bd4fe5ae855311b8b284fad2fe0085856edda03449a1a8'
        'd808e3c4e333076402d5692d2dfd122c4e7920070707099f9afde43fdcd9fdfdfb8787fbb6300f8ce23660e1d9b9a62a54078452438f4df889b404d31ed3b759'
        'e8e203b82222a6da8b66fa5f4d0f8e470af676d522a789bb32c56db5e6abfcf38b432a12aca42467ec91652f75d9b79957c58ebf5b0913591cf09a5afeaca2ea'
        '5418fe198e869b9f7e81e841328919f8f761e216cbb83551b75bd045f0beacaa546a795a3364a75d91e6cc535aba83b4dadd7fb6b8211aebac30f98b55c14bf1'
        '6a96d33517287ddd86f7277dcf84a062436dbae1b92a2b433304d80d487330df98ff990f8592696bd5a57f2254a9e34103fee17326679e3c4d54d2e60df3a76d')
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
