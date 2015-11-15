# Maintainer: Andrey Vihrov <andrey.vihrov at gmail.com>

pkgname=xfdashboard
pkgver=0.5.3
pkgrel=1
pkgdesc="Maybe a Gnome shell like dashboard for Xfce"
arch=('i686' 'x86_64')
url="http://goodies.xfce.org/projects/applications/xfdashboard/start"
license=('GPL')
depends=('libwnck3' 'clutter' 'garcon' 'xdg-utils')
makedepends=('intltool')
install="xfdashboard.install"
source=("http://archive.xfce.org/src/apps/${pkgname}/0.5/${pkgname}-${pkgver}.tar.bz2")
sha256sums=('a11625fec3e0ef61dbfd8c5af47df1dec55a92cbcaccba1f446058feeb629b4b')

build() {
  cd "${pkgname}-${pkgver}"

  ./configure --prefix=/usr --sysconfdir=/etc --disable-dependency-tracking
  make
}

package() {
  cd "${pkgname}-${pkgver}"

  make DESTDIR="${pkgdir}" install
}

# vim:set ts=2 sw=2 et:
