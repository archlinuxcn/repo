# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-dict-nightly
_pkgbase=${pkgbase%-dict-nightly}
pkgname=(rime-wanxiang-dict-nightly rime-wanxiang-pro-dict-nightly)
pkgver=13.1.9+r20251026.002714
_schema_version=${pkgver%%+*}
pkgrel=1
pkgdesc="万象词库——每日构建版"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${_schema_version}.tar.gz"
        build.sh)
b2sums=('9e016ab7f5ca52447045acd6a5d56b7f2c1328ad579c21e298b141b6891bbaf741d2fbee73ed5ac111ba739bdb74ed6ecf382bee2c5b2ca7460602ceb71e1511'
        'e1c0a4adf4a6175ac1343c9d94d5deb6d3e134b5258111849cc714893bb1fb70d308ffb900969e510087c59489318678a3e4ad88c8a134f03d90722a1202a672'
        '4622eeb0d8aa3971ee5122cf73e77b410c726f541435f43edc9f49f9e3b9ef58d16c793a5afd56740b235c9aa1d29fe31b55dc76c022a05cf074e67471012ab2'
        'a4d3d174fade99c71dae7f59b397443d8de7555cd5f04581514ed5b9e1f1c31ad1a76a079d196bf55ca45f0fdaf74bf29764d68e309dc0e270e71ef4ea8b6789'
        'a20608436baebabe153287426acb0d30a9b59a6a3bc3ec3243c75c22a897f01e2476a325c075874bd598844dfaac619f7856cc64f74ecc89572a01f469f87bdd'
        '9936422ff7591101eaf4bfc93ed3029e30c76b4a432b0db756f769997e3171484b14e0848890df0a876ff0d4090950d09fa2ef2eda9424cd2e7f12f30b6666e7'
        '1f843c82f6910b981354bc5f3f125a0eeb8f1de4bca9080f0a8652a012b3bd22baa9d02877610d93a65541fe202ced0ab9ebfd4205d7ead5f75c499862e2c071'
        '2f23b5c74ce8a4440abe2f3bb15502f6e3981590c8929448402f3365c2de749c909586748cf536d5796995b6b399e2f49aea87f6e466e3f9e34b6fbe17a25543'
        '75854ed0363db96e48f398751a955b8652638592bcf1362e8e2ed001ed97bb201fc892c11c64c47553246b88f91305d98bd7cdfa495bfc2891bde1d3d0cc0595')
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
