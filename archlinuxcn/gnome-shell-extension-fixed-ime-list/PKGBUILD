# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=gnome-shell-extension-fixed-ime-list
pkgver=6
pkgrel=1
pkgdesc="Make the IME list in fixed sequence instead of MRU."
arch=('any')
url="https://github.com/AlynxZhou/gnome-shell-extension-fixed-ime-list"
license=('GPL')
depends=('gnome-shell')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=('09dcfb573e9f1ab6b341fbdf151d9578cf9db28beb5704dccdfdde29482c70e0a6b6d83752778228ea57bcaf1118a16bfe4fbdd022908590b891b38092642e68')

package() {
    _uuid="fixedimelist@alynx.one"

    install -d "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
    cd "${srcdir}/${pkgname}-${pkgver}"
    cp -a * "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
}

