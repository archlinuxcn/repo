# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-dict-nightly
_pkgbase=${pkgbase%-dict-nightly}
pkgname=()
pkgver=8.8.1+r20250715.234247
_schema_version=${pkgver%%+*}
pkgrel=1
pkgdesc="万象词库每日构建版"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${_schema_version}.zip")
b2sums=('518ba90a65839413ec3f762f928ed56adff0aff68cd712051d3b98d1340f11a9a6eae2d5b7cb63f5223c066f2994bd5ed0cdbb12c814864f0085f10d2b502adf'
        'af98a95b71e86c1174d874341092a7ad765c09ff43527e11cb128d81b3c1498062a0b5a9b580d6cc6d78efad91af55be4f011ec731627614b20c90d42783a282'
        '5c97de47c8f73564909e6f9c089cd334784b580acca3ee3a879b3d816319d7d480cd1dce2ba66de1c2a70e7a7b14885086080dab91f215ec0cfda90d291508cc'
        '4f079767d5afeb2ace829bf897ddd9a30a2025d9867d4dad67e4becea5c5aea0ababc7851d8a7fa2c93e4e6423179b578e68d8e5fdc3ac6ab9a8b96d8bf5f868'
        'ac670fc74a9a5931285bb96abd3365410a3cc87a694ef10fee60a74226166c5989ad6ca006abe3465dae3b4f5a62261675dc40bcbe6876df6c1a4cc05269b1f9'
        'a3fcedf9e849a11e9f3f829c5a58c2e0d7e810a23a90661005e7588f4fb6a04eaf4a778dbc2f42092e2c9cb929d3fa24d25464c3632566ab2bd111c37dd2a7a5'
        '1d672d3eb90fc80cc74b842f126a96b73ace03626765fc94d05a28f497ef8d2e3588f9c96f6541f8853918a8bcee66c1ee73150ac637ebd46c263960ac759e0d'
        'd8298859265c2953e45b933a50dc02c2312afffba81340133475dead2381d886a14849d8432683ec83572db81f5044234050bb06ae788bacf722dc671f37c831'
        'fadfbe5802a0061ee8d2e24b76f6c5455e0bc5f893be05c23776cf80775a9080843846cf297b6a36d488d1059f1761d45432349d7ebacab7ca8033ce00d4c29c')

makedepends=("librime" "rime-prelude" "rime-essay" "sed" "python" "zip")

declare -A _dict_filenames=(
  [moqi]="1-pro-moqi-fuzhu-dicts.zip"
  [flypy]="2-pro-flypy-fuzhu-dicts.zip"
  [zrm]="3-pro-zrm-fuzhu-dicts.zip"
  [jdh]="4-pro-jdh-fuzhu-dicts.zip"
  [tiger]="5-pro-tiger-fuzhu-dicts.zip"
  [wubi]="6-pro-wubi-fuzhu-dicts.zip"
  [hanxin]="7-pro-hanxin-fuzhu-dicts.zip"
  [base]="9-base-zh-dicts.zip"
)

for _dict in "${!_dict_filenames[@]}"; do
    _filename="${_dict_filenames[${_dict}]}"
    source+=("${url}/releases/download/dict-nightly/${_filename}")
done

build() {
    cd "${srcdir}/rime_wanxiang-${_schema_version}" || exit 1
    bash .github/workflows/scripts/release-build.sh
}

# 基础版中文词库
_pkgname=${_pkgbase}-dict-zh-nightly
pkgname+=("${_pkgname}")
eval "package_${_pkgname}() {
    pkgdesc='万象拼音中文词库每日构建版（标准版）'
    provides=('${_pkgname%-nightly}=${_schema_version}')
    conflicts=(${_pkgname%-nightly})
    replaces=(rime-wanxiang-dict-cn-nightly)

    _package_dict_zh base
}"

declare -A _fuzhu_names=(
  [zrm]="自然码"
  [moqi]="墨奇"
  [flypy]="小鹤"
  [jdh]="简单鹤"
  [hanxin]="汉心"
  [wubi]="五笔前2"
  [tiger]="虎码首末"
)

# Pro 中文词库
for _fuzhu in "${!_fuzhu_names[@]}"; do
    _fuzhu_name="${_fuzhu_names[${_fuzhu}]}"
    _pkgname=${_pkgbase}-pro-dict-zh-${_fuzhu}-nightly
    pkgname+=("${_pkgname}")
    _conflicts=("${_pkgname%-nightly}")
    for _fuzhu_c in "${!_fuzhu_names[@]}"; do
        if [[ "${_fuzhu_c}" == "${_fuzhu}" ]]; then continue; fi
        _conflicts+=("${pkgbase}-pro-dict-zh-${_fuzhu_c}-nightly")
    done
    eval "package_${_pkgname}() {
        pkgdesc='万象拼音中文词库每日构建版（${_fuzhu_name}辅助码版）'
        provides=('${_pkgname%-nightly}=${_schema_version}')
        conflicts=(${_conflicts[*]})

        _package_dict_zh pro $_fuzhu
    }"
done

_build_dicts() {
    for _f in $(pacman -Qql rime-prelude rime-essay | grep -v "/$"); do ln -sf "${_f}" .; done

    for _s in "$@"; do rime_deployer --compile "${_s}"; done

    find . -type l -delete
    rm build/*.txt
}

_package_dict_zh() {
    _type=$1
    _fuzhu=$2

    _dist_dir="rime-wanxiang-base"
    _dict_src_dir="zh_dicts"
    _dict_dir="zh_dicts"
    if [[ $_type == 'pro' ]]; then
        _dist_dir="rime-wanxiang-${_fuzhu}-fuzhu";
        _dict_src_dir="pro-${_fuzhu}-fuzhu-dicts"
        _dict_dir="zh_dicts_pro"
    fi
    cd "${srcdir}/rime_wanxiang-${_schema_version}/dist/${_dist_dir}" || exit 1

    rm ./${_dict_dir}/*
    install -Dm664 "${srcdir}/${_dict_src_dir}/"* -t ./${_dict_dir}/

    find . -type f \( \
        -path "./zh_dicts*" -o \
        -path "./wanxiang.*.yaml" -o \
        -path "./wanxiang_pro.*.yaml" -o \
        -path "./wanxiang_lookup.*.yaml" -o \
        -path "./wanxiang_symbols.yaml" \
        \) \
        -exec install -Dm664 {} "${pkgdir}"/usr/share/rime-data/{} \;

    pushd "${pkgdir}"/usr/share/rime-data/
        _build_dicts wanxiang*.schema.yaml
        rm -f ./*.schema.yaml ./{wanxiang,wanxiang_pro}.dict.yaml ./wanxiang_symbols.yaml
    popd
}
