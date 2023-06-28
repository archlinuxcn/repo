# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=gnome-shell-extension-net-speed
pkgver=8
pkgrel=1
pkgdesc="Show current net speed on panel."
arch=('any')
url="https://github.com/AlynxZhou/gnome-shell-extension-net-speed"
license=('GPL')
depends=('gnome-shell')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=('07b21c3e968be6d5e983cb2d7a6faa07d72f499ca0e0dbf99d0105f2f846a1c9338f1d15ae12ce9dd6798e22dd2c0ccb90b46f1321891919a360939b43e17b72')

package() {
    _uuid="netspeed@alynx.one"

    install -d "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
    cd "${srcdir}/${pkgname}-${pkgver}"
    cp -a * "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
}
