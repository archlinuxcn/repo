# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-dict-nightly
_pkgbase=${pkgbase%-dict-nightly}
pkgname=()
pkgver=8.7.5+r20250713.110501
_schema_version=${pkgver%%+*}
pkgrel=1
pkgdesc="万象词库每日构建版"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${_schema_version}.zip")
b2sums=('82837e2c658e0590b5ff3e2539012cfb45789e287155f8d12781a7cc23c596309237f9e4f414747983820a266177eb8e5339318ef0c38f502cec4f8df7da4f0b'
        '7a8b1f2227134d59f6da1883f453410455fc93d8f7eb730743c790acb020c070a40599198287a1486d451c08e62b645c9c32efd23ee9c361c3c47c902d29993b'
        'b6ca73904daa04a753289ffe3530f8a7078dab5d59578a723516cdaf20e07ea0c2005a43b1d3909c75a8cbdccc23025c18e05a581e44bf41d394921acf514942'
        '7889a69873b4245bfbaf141760622beec18aca19c3a2dbdebe8c98fe24b0ea394bd925a3d0d7c4a16334941c56006ccb9c5f113047498d702da2cdfc4bf7b111'
        '0ad183a4c819e6d5c753f94186bc6eba4f4a99ad9929145452f096dfafa48b381a0e73bf4fcc734630c69b127f4f235a6e4e609217a06c1fdc60131eeff41ebc'
        '410cb8018c49510e5126380764758d40cb2879157d9d0cfd1946b08379ecd61f3b1d07363fc5de5b44be15340cfdb8538cf8f751cad6f1d0db6ddc944b4f55b3'
        'dedd840bdf985fccd58f3972ea2a155ec4c491faa879d5d39adebd0fe5f7ae648382878515413692c69e4c77e99a96babf123ca7644b0b480b2090082f3dfafa'
        'fc4f722cb3c58cdcc11731bf4f5feb9333c779bd8b8a6e2f3fb67fde184b1781b69df439c5fb9ec450fdfb56da81982fae4e85ff7e4aa852f411d2bc345aa4cb'
        '101ac9fba3e36d2bb433e0df2a4d13a5d9217e9297161fe4ecc13b94260c8e42286fd19dd663dd1f2ec08d921eafeda804cc0c867a9617223166031793459c3e')

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
        rm -f ./*.schema.yaml ./wanxiang*.dict.yaml ./wanxiang_symbols.yaml
    popd
}
