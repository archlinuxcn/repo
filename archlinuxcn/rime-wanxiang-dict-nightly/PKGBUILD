# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-dict-nightly
_pkgbase=${pkgbase%-dict-nightly}
pkgname=()
pkgver=8.7.2+r20250709.235543
_schema_version=${pkgver%%+*}
pkgrel=1
pkgdesc="万象词库每日构建版"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${_schema_version}.zip")
b2sums=('b8ef1c7292d6d5ef0f5d149f5a74fd3936b1c2e46f57aa3456fdfeec1e74feeffc4691ebcbe2c1731697cc5181c2fb6d8cf1a3077d576ebd3799042c42691768'
        '0684e03f523e2dd09ea4008090f1a9c4b998fef06ea3200cc9469c7368ed643d1fe3f6fc619e1c38fcd83d486b81239bba5a34a2c3386a68b54bd1341f65edea'
        'd06a94fde209b8d1e026461b94e7238f7bfbb5d1db2e358638ebd8beb270a43fff161282791e205c7be2284282592a4e034881d762bb736fe88a65f02a43e582'
        '756bc87d57aeebd11fff935380ac3da15b4c2ce7c5a06fc8c451007a026afd857e256eb73a25692bcb626cfe5184c47229bb9f6a54507bf9de5e716b3a6ff5ea'
        '58b94337cea9631c69d48ee5851f62edcde080fe55be2357f6ae37a50dc0dc24bd5318943fcc51d3bd66475022ef5a03b5ec937b8bbf1ff908d9acb789084af8'
        '159e0398cdc80d876ddcb7b02bbf39976538989aa212fb13ea6428136c4ce881c703bc88041cdb4d5ddc6223649c196824f3671cb13998c5d850949c63bce0ee'
        '1315fcc17c9bc4e6a34fd3773222ccf67d7cfbc2475a8b22a6192e8b68f847bdcdb80da6853dc2f536eb776a0870b7fd35aee24409225b7f411bb4bda947ccf6'
        '46aa6a19ab25c91cd7005bf6f668033a364d81e05764f20a4348b39a8ddbb40c5496d4d667e63be49fb3af4e38c1bc2f7c279260bf7c956c82966e331ff59619'
        '30a39e222baf342ea5301634165cd76aad8cd508650097ee14002d0cfda6b71c019b4f0500366d9c47dede7454e296a830fe6f3b076c981e28b20676accc60e8')

makedepends=("librime" "rime-prelude" "rime-essay" "sed" "python")

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
