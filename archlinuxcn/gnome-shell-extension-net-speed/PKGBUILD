# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=gnome-shell-extension-net-speed
pkgver=7
pkgrel=1
pkgdesc="Show current net speed on panel."
arch=('any')
url="https://github.com/AlynxZhou/gnome-shell-extension-net-speed"
license=('GPL')
depends=('gnome-shell')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=('a5827cae09d6be1adee4f7871b43f3d6fee932dbcfb576d30eaa22781d67b9eac14e2b94ff1962419e141cfe5bd6c8605273eb3782876160451d48342ab6138b')

package() {
    _uuid="netspeed@alynx.one"

    install -d "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
    cd "${srcdir}/${pkgname}-${pkgver}"
    cp -a * "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
}
