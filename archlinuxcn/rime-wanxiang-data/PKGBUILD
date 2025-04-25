# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang-data
pkgname=(rime-wanxiang-data
         rime-wanxiang-gram-zh-hans
         rime-wanxiang-dict-cn)
_schema_version=6.5.3
_dict_version=20250424
pkgver=6.5.3+r20250424
pkgrel=1
epoch=1
pkgdesc="万象词库"
arch=(any)
license=('CC-BY-4.0')
url="https://github.com/amzxyz/RIME-LMDG"
source=("wanxiang-lts-zh-hans.${_dict_version}.gram::${url}/releases/download/LTS/wanxiang-lts-zh-hans.gram"
        "cn_dicts.${_dict_version}.zip::${url}/releases/download/dict-nightly/cn_dicts.zip"
        "https://github.com/amzxyz/rime_wanxiang/archive/refs/tags/v${_schema_version}.tar.gz")
sha256sums=('20f2ecb4d5ed29471ba9ff1aa34838a6d5604a0b9bddf1f8c64ef1c2998d7eec'
            '59c85a2bcbc0e693aeae9f078b0123b05198bad775f2064b175e325f0f403e72'
            '03f6a11a8e1004036b37a2d1ae6dde43df3fe25df2faa446cf155c003c3c2223')

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
