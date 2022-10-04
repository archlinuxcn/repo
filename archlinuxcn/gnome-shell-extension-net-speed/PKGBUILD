# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=gnome-shell-extension-net-speed
pkgver=5
pkgrel=1
pkgdesc="Show current net speed on panel."
arch=('any')
url="https://github.com/AlynxZhou/gnome-shell-extension-net-speed"
license=('GPL')
depends=('gnome-shell')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=('d71ce903b7dcaad79d15ec4153d5d4703a0a3f62fd3ae63c4efcc9bd8933fcb47ecc08d8710ad2553738f73af38e4602892525ae48911067e2a47c75a5355856')

package() {
    _uuid="netspeed@alynx.one"

    install -d "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
    cd "${srcdir}/${pkgname}-${pkgver}"
    cp -a * "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
}
