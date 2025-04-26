# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-data
pkgname=(rime-wanxiang-data
         rime-wanxiang-gram-zh-hans
         rime-wanxiang-dict-cn)
_schema_version=6.5.5
_dict_version=20250425
pkgver=6.5.5+r20250425
pkgrel=1
epoch=1
pkgdesc="万象词库"
arch=(any)
license=('CC-BY-4.0')
url="https://github.com/amzxyz/RIME-LMDG"
source=("wanxiang-lts-zh-hans.${_dict_version}.gram::${url}/releases/download/LTS/wanxiang-lts-zh-hans.gram"
        "cn_dicts.${_dict_version}.zip::${url}/releases/download/dict-nightly/cn_dicts.zip"
        "https://github.com/amzxyz/rime_wanxiang/archive/refs/tags/v${_schema_version}.tar.gz")
sha256sums=('0de368de2a399fb307b62c11f0bc8887d4063e9392b9d3eb3b9e3477c37a4bab'
            'cadbf9c54c4016fa9b6bbd7fc45dbd06164939d6ac46c891c0c5a9bd1c510607'
            '37dfc20fba4fc59dfca73cc9b15bdbe50835ff0d24f87c8386fc10e6e5f940db')

makedepends=("librime" "rime-prelude" "rime-essay" "sed")

build() {
    cd "${srcdir}/rime_wanxiang-${_schema_version}"

    rm -r cn_dicts
    cp -r "${srcdir}/cn_dicts" .

    for _f in $(pacman -Qql rime-prelude rime-essay | grep -v "/$"); do ln -sf $_f; done

    rime_deployer --compile wanxiang.schema.yaml

    find . -type l -delete
}

package_rime-wanxiang-data() {
    pkgdesc="万象词库 Meta 包"
    depends=("rime-wanxiang-gram-zh-hans" "rime-wanxiang-dict-cn")
}

package_rime-wanxiang-gram-zh-hans() {
    pkgdesc="万象词库——语法模型"
    replaces=(rime-lmdg)

    install -Dm664 "${srcdir}/wanxiang-lts-zh-hans.${_dict_version}.gram" "${pkgdir}"/usr/share/rime-data/wanxiang-lts-zh-hans.gram
}

package_rime-wanxiang-dict-cn() {
    pkgdesc="万象词库——中文词库"

    cd "${srcdir}"

    find cn_dicts -type f -exec install -Dm664 {} "${pkgdir}"/usr/share/rime-data/{} \;

    install -Dm664 "rime_wanxiang-${_schema_version}"/build/wanxiang.*.bin -t "${pkgdir}"/usr/share/rime-data/build
}
