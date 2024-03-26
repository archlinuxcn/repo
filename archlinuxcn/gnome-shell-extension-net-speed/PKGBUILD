# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=gnome-shell-extension-net-speed
pkgver=10
pkgrel=1
pkgdesc="Show current net speed on panel."
arch=('any')
url="https://github.com/AlynxZhou/gnome-shell-extension-net-speed"
license=('GPL')
depends=('gnome-shell')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=('c22ae77883781cfa7f4536228e24b765a0f9686ea3ce67c368685e9f948e819f4678df1c93c74a49c471a3c168cad4eb573c2a4a2cd69d0edf96bf2e7df22503')

package() {
    _uuid="netspeed@alynx.one"

    install -d "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
    cd "${srcdir}/${pkgname}-${pkgver}"
    cp -a * "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
}
