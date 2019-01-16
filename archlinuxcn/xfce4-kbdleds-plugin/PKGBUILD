# Maintainer: Raphael Scholer <rscholer@gmx.de>
# Contributor: tomberry88 <tomberry@live.it>
# Contributor: Gour-Gadadhara Dasa <gour@atmarama.net>
pkgname=xfce4-kbdleds-plugin
pkgver=0.0.6
pkgrel=8
pkgdesc="Xfce keyboard LEDs panel plugin"
arch=('i686' 'x86_64')
url="http://goodies.xfce.org/projects/panel-plugins/xfce4-kbdleds-plugin"
license=('GPL2')
conflicts=("xfce4-kbdleds-plugin-git")
depends=('xfce4-panel')
makedepends=('intltool')
source=("http://git.xfce.org/panel-plugins/${pkgname}/snapshot/${pkgname}-${pkgver}.tar.bz2")
install="${pkgname}.install"
sha256sums=('2c36c6ac5ef2bd564058e6040888b21a67939ba79041249d10a9ccc2b6b6bca2')

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
