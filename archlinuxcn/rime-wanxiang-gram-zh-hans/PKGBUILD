# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgname=rime-wanxiang-gram-zh-hans
pkgver=20261110.092242
pkgrel=1
epoch=2
pkgdesc="万象词库中文语法模型"
arch=(any)
license=('CC-BY-4.0')
url="https://github.com/amzxyz/RIME-LMDG"
source=("wanxiang-lts-zh-hans.${pkgver}.gram::${url}/releases/download/LTS/wanxiang-lts-zh-hans.gram")
sha256sums=('3457b69f5fe0fc4f5d211c878bbfa2e2361b90639952c9845c8e31e9d047cde6')

package_rime-wanxiang-gram-zh-hans() {
    replaces=(rime-lmdg)

    install -Dm664 "${srcdir}/wanxiang-lts-zh-hans.${pkgver}.gram" "${pkgdir}"/usr/share/rime-data/wanxiang-lts-zh-hans.gram
}
