# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-dict-nightly
_pkgbase=${pkgbase%-dict-nightly}
pkgname=()
pkgver=9.2.2+r20250723.150217
_schema_version=${pkgver%%+*}
pkgrel=1
pkgdesc="万象词库每日构建版"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${_schema_version}.zip")
b2sums=('e3ea73e6f15cc9b93a92193f5ae0c20f1df274d6f43f22bd0961e78e93b5f2ce138e5c8c64b0cfa88e77805917edd53b32dfb8eeb708e9178690de011ad10624'
        '9edb9b94743a8ee331452c89e63fc01a536dd84f066d6d8143cadbf03dd1fc3d1407ef90c174d4dd9c30d5e95cf03bf11cf8e50aa8170f361e16e6d033a05c6d'
        '7c317b0922438d3f5bc9e7f4eff45ce0509ee518655c8db310b1f292b7621bec144bfb9a8013cf94e5c171ce2302aa9251a05dc463c3a77baba21fcfabe3a76e'
        '08b5e38878cebcb6f46ff913a041994243363451321cc4e5e413711e1a623b01dad941bc81c695a8d96522318a9d2ae8f3ad17428a624e79110e8672fd26eae7'
        'c853f6ac3c39d525b08d2daf65df81fcf112c0ab100fe44bf6fc3af2e355cabc07cf2fd8f32c4df3d821c314ba54c893b02af0eb564808d2eb3d8c0928a85544'
        '8e426b1de2ac7cf323ec83cfbf36c915e80bb4b84d763396d0b624faf8beec4b27edd0a874b5e9052e36f86f8655d2f1d9cc6d88159850ba5e19d753a1d005f5'
        'eb233309b94659ca9408cb3470c884480e0e130cb508a90b6ad4da24a78eec63e6025b13c9a37170b5f212dd766204055ac68f274b082c71f350bb0487d2b51c'
        '877bc754e8d1e482fc1bbc7396e3ab4ae21c256ea74fc68cf40e5b001456f59b441ee8ba7fccc56d1f0abdc9c1ab5b27c0f4681018119f3911b55961149f0ae2'
        'bef4cc762585d152ed2a9d3191aabf23a1b062379b4c3ed7380fa991e19606dec719250382986d2cd3201de5a327a70eaf8d0e64e3540ba098b66929bff348a6')

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
