# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgname=rime-wanxiang-gram-zh-hans
pkgver=20251013.180551
pkgrel=1
epoch=2
pkgdesc="万象词库中文语法模型"
arch=(any)
license=('CC-BY-4.0')
url="https://github.com/amzxyz/RIME-LMDG"
source=("wanxiang-lts-zh-hans.${pkgver}.gram::${url}/releases/download/LTS/wanxiang-lts-zh-hans.gram")
sha256sums=('d1a0c93110f0c337a30368d4cf3152cda8981ee2fb4e4a7b0f5ea8780bf7c73e')

package_rime-wanxiang-gram-zh-hans() {
    replaces=(rime-lmdg)

    install -Dm664 "${srcdir}/wanxiang-lts-zh-hans.${pkgver}.gram" "${pkgdir}"/usr/share/rime-data/wanxiang-lts-zh-hans.gram
}
