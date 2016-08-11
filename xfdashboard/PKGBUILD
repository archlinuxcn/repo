# Maintainer: Andrey Vihrov <andrey.vihrov at gmail.com>

pkgname=xfdashboard
pkgver=0.6.0
pkgrel=3
pkgdesc="Maybe a Gnome shell like dashboard for Xfce"
arch=('i686' 'x86_64')
url="http://goodies.xfce.org/projects/applications/xfdashboard/start"
license=('GPL')
depends=('libwnck3' 'clutter' 'garcon')
makedepends=('intltool')
source=("http://archive.xfce.org/src/apps/${pkgname}/${pkgver%.*}/${pkgname}-${pkgver}.tar.bz2")
sha256sums=('86feda138001a3bbb686a36c14ad6923e3c7ab2c1b921217f9c075cd43c2b1bc')

build() {
  cd "${pkgname}-${pkgver}"

  ./configure --prefix=/usr --sysconfdir=/etc --disable-dependency-tracking
  # -Wl,--as-needed should come before all libraries
  sed -i -e '/\$CC/s/-shared/\0 -Wl,--as-needed/' libtool
  make
}

package() {
  cd "${pkgname}-${pkgver}"

  make DESTDIR="${pkgdir}" install
}

# vim:set ts=2 sw=2 et:
