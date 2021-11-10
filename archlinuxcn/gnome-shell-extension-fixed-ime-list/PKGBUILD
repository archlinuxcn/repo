# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=gnome-shell-extension-fixed-ime-list
pkgver=7
pkgrel=1
pkgdesc="Make the IME list in fixed sequence instead of MRU."
arch=('any')
url="https://github.com/AlynxZhou/gnome-shell-extension-fixed-ime-list"
license=('GPL')
depends=('gnome-shell')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=('4bcd80233ce474130c543a0a9a403f658fe10b0c3c3d208c141bac423aac80b04021a035d60a15598783ccd0414eb97abf3d5ca72f66621d502fe08d38da02b4')

package() {
    _uuid="fixedimelist@alynx.one"

    install -d "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
    cd "${srcdir}/${pkgname}-${pkgver}"
    cp -a * "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
}

