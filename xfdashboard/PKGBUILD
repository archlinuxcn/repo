# Maintainer: Andrey Vihrov <andrey.vihrov at gmail.com>

pkgname=xfdashboard
pkgver=0.5.91
pkgrel=1
pkgdesc="Maybe a Gnome shell like dashboard for Xfce"
arch=('i686' 'x86_64')
url="http://goodies.xfce.org/projects/applications/xfdashboard/start"
license=('GPL')
depends=('libwnck3' 'clutter' 'garcon' 'xdg-utils')
makedepends=('intltool')
install="xfdashboard.install"
source=("http://archive.xfce.org/src/apps/${pkgname}/${pkgver%.*}/${pkgname}-${pkgver}.tar.bz2")
sha256sums=('48033a24b838d52b0f02eae886153cd6188ff55035e3dbcbf01ffd3bb1765bfb')

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
