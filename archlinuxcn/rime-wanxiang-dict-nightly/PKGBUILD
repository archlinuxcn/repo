# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-dict-nightly
_pkgbase=${pkgbase%-dict-nightly}
pkgname=()
pkgver=9.0.1+r20250719.093638
_schema_version=${pkgver%%+*}
pkgrel=1
pkgdesc="万象词库每日构建版"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${_schema_version}.zip")
b2sums=('143c5080752706fbbaecf11ffc52386068b097a11d12b077b5dc1a65af29abbf195074abccbe074fc2a5713a334fddaa4a28f6c87a833643b444dbd45b320034'
        '823e4b268cee2bc81e2a2ff4e5c0d52071a3b72eb78b4e5ac8d5c83898c4dc454d9fef17ddccdab608db3e8b617d19081667e2ecd0dfc7f891d78da9f0632993'
        '28066a4a5f49aa7769d9ecbdcd30d6273f8d286427d68b538c5e97238b44e4760aafddce123121197ed0d5dcd0a303bd5d48650b26e66c24f231455ada1da240'
        '2838e79ebd58fccd273d68030b748d6b758272012cb0fbbef852448186d988b55788fbaf6e556e715c434eda6cd1d83a240e17fb6c2e58e08509eebc547cb9e6'
        'def0672565741902db5c056e3903e7ff6a2e6eb144bb84be1db2352e3cbb8642ae1466ee074a32d80e0793cc92f007e934ce6216cf62500f7c97b006e4129718'
        'ff1ac2fdaa1f8c04cde63772ee1a64fe7cb74dce989a077f3a146cc958307994951d66474cb2f3945f982a5c74d0081267df3670316bd53836e35dbd7efe6d5d'
        '51b57a3dbfb5c95f07de4e0fec073c9619b860686633d5bbccdaa030d5af21acabcfb65695bacdacc5a19a0213b9a61cc3f3234ae0bc7d2d74f6d031670f16c7'
        'dd333453bba1555c88e321bd20991ab59ddd8a75df5e526c21090482df4f7002034fcbf4c7bbce3f69f83539c13509166507de7ebaa6c4d5af6b388fbe99d176'
        '236557daf4f3c21d59e089476236e213a258c96e250e15470a5ecfe90eeae8fc688ed0da96135c049dce2462894f74fb7383daa7f7fd1695b8dd44bb26fd13d5')

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
