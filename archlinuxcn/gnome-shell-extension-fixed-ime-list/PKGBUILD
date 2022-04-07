# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=gnome-shell-extension-fixed-ime-list
pkgver=8
pkgrel=1
pkgdesc="Make the IME list in fixed sequence instead of MRU."
arch=('any')
url="https://github.com/AlynxZhou/gnome-shell-extension-fixed-ime-list"
license=('GPL')
depends=('gnome-shell')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=('d54e2cfbc5c4427f772c7be906b7445eccb3dc83a0414b9b6841eabeb5828f9c4b535ab344b43c549e04f8085f0310fea2ee34cdcb89ce3a9b6f269129421228')

package() {
    _uuid="fixedimelist@alynx.one"

    install -d "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
    cd "${srcdir}/${pkgname}-${pkgver}"
    cp -a * "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
}

