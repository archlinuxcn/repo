# Maintainer: Andrey Vihrov <andrey.vihrov at gmail.com>

pkgname=xfdashboard
pkgver=0.5.92
pkgrel=1
pkgdesc="Maybe a Gnome shell like dashboard for Xfce"
arch=('i686' 'x86_64')
url="http://goodies.xfce.org/projects/applications/xfdashboard/start"
license=('GPL')
depends=('libwnck3' 'clutter' 'garcon' 'xdg-utils')
makedepends=('intltool')
install="xfdashboard.install"
source=("http://archive.xfce.org/src/apps/${pkgname}/${pkgver%.*}/${pkgname}-${pkgver}.tar.bz2")
sha256sums=('682a3bb447d4ed1e558e30ae4b8526bcb89f053baf8d1081531a39091d835efd')

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
