# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=gnome-shell-extension-fixed-ime-list
pkgver=4
pkgrel=1
pkgdesc="Make the IME list in fixed sequence instead of MRU."
arch=('any')
url="https://github.com/AlynxZhou/gnome-shell-extension-fixed-ime-list"
license=('GPL')
depends=('gnome-shell')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha512sums=('091683e564468a6b2d171b93af089fce08075dc318010167fe689300ab47f610b9a74696e637f95313db74593ac0de442dc9e1cba5e6de4177eb3b4a3fb05dc5')

package() {
    _uuid="fixedimelist@alynx.one"

    install -d "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
    cd "${srcdir}/${pkgname}-${pkgver}"
    cp -a * "${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"
}

