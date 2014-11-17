# Maintainer: Edoardo Maria Elidoro <edoardo.elidoro@gmail.com>
# Contributor: Piotr Rogoża <rogoza dot piotr at gmail dot com>
# Contributor: Tobias Kieslich <tobias (at) archlinux.org>

pkgname=xfce4-xfapplet-plugin
pkgver=0.1.0
pkgrel=8
pkgdesc="plugin that allows to use gnome applets in the Xfce4 panel"
arch=('i686' 'x86_64')
license=('GPL2')
url="http://xfce-goodies.berlios.de/"
groups=('xfce4-goodies')
depends=('xfce4-panel' 'libxfcegui4' gnome-panel2) 
source=(http://archive.xfce.org/src/panel-plugins/${pkgname}/0.1/${pkgname}-${pkgver}.tar.bz2)
md5sums=('6a06c44b18a97626f44a240ad3bc3244')

build() {
  cd ${srcdir}/${pkgname}-${pkgver}
  ./configure --prefix=/usr \
	--sysconfdir=/etc \
	--libexecdir=/usr/lib/ \
	--localstatedir=/var \
	--disable-static \
	--disable-debug
  make
}

package() {
  cd ${srcdir}/${pkgname}-${pkgver}
  make DESTDIR=${pkgdir} install
}
