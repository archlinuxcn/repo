# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=gnome-shell-extension-shuzhi
_pkgname=shuzhi
pkgver=40
pkgrel=1
pkgdesc="A wallpaper generation extension for gnome shell, inspired by Jizhi."
arch=('any')
url="https://github.com/tuberry/shuzhi"
license=('GPL3')
depends=('gnome-shell')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha512sums=('b67d01e48ae9ba7d71fe400b6a3f0c188b955e1010c23a1464dda0bc3d627587e2105828079706227602e8cee22ca58f915d2bf0bf29868da46128915269c61b')

build() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	make
}

package() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	make DESTDIR="${pkgdir}/" install
}
