# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgname=rime-wanxiang-gram-zh-hans
pkgver=20260627.005556
pkgrel=1
epoch=2
pkgdesc="万象词库中文语法模型"
arch=(any)
license=('CC-BY-4.0')
url="https://github.com/amzxyz/RIME-LMDG"
source=("wanxiang-lts-zh-hans.${pkgver}.gram::${url}/releases/download/LTS/wanxiang-lts-zh-hans.gram")
sha256sums=('e178d9493e0f4ba4fabd3280338ad06e0934a89b5ac1667fbc7db7c5c2cd003a')

package_rime-wanxiang-gram-zh-hans() {
    replaces=(rime-lmdg)

    install -Dm664 "${srcdir}/wanxiang-lts-zh-hans.${pkgver}.gram" "${pkgdir}"/usr/share/rime-data/wanxiang-lts-zh-hans.gram
}
