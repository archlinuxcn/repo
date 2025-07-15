# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-dict-nightly
_pkgbase=${pkgbase%-dict-nightly}
pkgname=()
pkgver=8.8.0+r20250715.234247
_schema_version=${pkgver%%+*}
pkgrel=1
pkgdesc="万象词库每日构建版"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${_schema_version}.zip")
b2sums=('e15cb31ec39717540c9e3955fdce0c1284a361f7466a5132bf148b9e648d27b2ae2f646af755aec12a08c79b717dd0fe8fd311da28087ccc315091c5bfa1a392'
        'ddf8e242def7ce1424504bffa099ef0b84d90a38bc0bff4249a71f2d4862b585f92a70e36d2bfe50b504fcba83aa7c06460b36f60324176e2a70b7c066b037fc'
        '52c9e360d7e09c27a1f92849ffe2d35e693fad9eac93caa7c5cc036f3676cb5397a25135c48a2f22cca68d31eb9f323e816b421d42c4cd3b3154f6d82c7d8e83'
        '10d93cd27721f67341ddaddf591719fda2c4e7d3198445a06bd38cbcf707b84ec6cfe7501afbf2c2f16ef9b94484b967268de4ebfc66fa8bf1574bee38f1acb0'
        '46e2f1608022aa19ef1c6678f4d94be43a78fbb5fd6e4e5cf73bbdf1c1d263eed1648d059fa1b5737190940c07e30eeef62af6410b76fa074e723a83c0130294'
        '609f9d0770cf7446bb8d899ac0ec907608443601f2ba6b38285dffabed1cb67a3ee8c63c3530397d1eb473325bdebd01c3d207d639fec32d101d142932e67689'
        '1ea02908d1ac2116b5b9c0134adb70478177f9d1cbc11aa8b34fb1b36b9b0deb9ddfd57312b0c2f4cc22a545e72d909ff7cfde767ee41cdc96ce853a27a59410'
        '8a891280c5035d2439be5bf78d45cec9c06dfe48079bd2f2f42bf0c0bbe9ac32045fb5cae3f21aa5747adff88e4bbc23c13a1c37e9db3f8cb1d6069c10afb437'
        '21e121f7fa9131f797e8e6068bd66f39c91bf62828291af5ecd80dd7b9a5b3cf92ed7d20332ba5f5407d73a1b40c49071688a15cbd68d6a3f817b237a895e6e2')

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
