# Maintainer: Raphael Scholer <rscholer@gmx.de>
# Contributor: tomberry88 <tomberry@live.it>
# Contributor: Gour-Gadadhara Dasa <gour@atmarama.net>
pkgname=xfce4-kbdleds-plugin
pkgver=0.0.6
pkgrel=11
pkgdesc="Xfce keyboard LEDs panel plugin"
arch=('i686' 'x86_64')
url="https://goodies.xfce.org/projects/panel-plugins/xfce4-kbdleds-plugin"
license=('GPL2')
conflicts=("xfce4-kbdleds-plugin-git")
depends=('xfce4-panel')
makedepends=('intltool')
source=("https://git.xfce.org/archive/${pkgname}/snapshot/${pkgname}-${pkgver}.tar.gz")
install="${pkgname}.install"
sha256sums=('21e8e37cd55c38d0e29cd9a0396b030926b86d4790dfbb1727818cd0da8ee888')

build() {
	cd "${pkgname}-${pkgver}"
	./configure --prefix=/usr
	make
}

package() {
	cd "${pkgname}-${pkgver}"
	make DESTDIR="${pkgdir}" install
}
# vim:set ts=2 sw=2 et:
