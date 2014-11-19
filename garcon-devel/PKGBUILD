# $Id: PKGBUILD 197969 2013-10-30 11:59:30Z allan $
# Maintainer: Evangelos Foutras <evangelos@foutrelis.com>
# Contributor: Xavier Devlamynck <magicrhesus@ouranos.be>

_pkgname=garcon
pkgname=${_pkgname}-devel
pkgver=0.3.0
pkgrel=5
pkgdesc="Implementation of the freedesktop.org menu specification"
arch=('i686' 'x86_64')
url="http://www.xfce.org/"
license=('LGPL')
groups=('xfce4')
depends=('glib2' 'libxfce4ui')
makedepends=('pkgconfig' 'intltool' 'xfce4-dev-tools')
replaces=('libxfce4menu')
conflicts=("${_pkgname}")
provides=("${_pkgname}=${pkgver}")
options=('!makeflags')
source=(http://archive.xfce.org/src/xfce/garcon/0.3/garcon-$pkgver.tar.bz2)
sha256sums=('59348179f3cb9589d13ba8d18d5746be421b311cab974ce057dfdef0365b1e55')

build() {
  cd "$srcdir/${_pkgname}-$pkgver"

  ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --libexecdir=/usr/lib \
    --localstatedir=/var \
    --disable-static \
    --disable-debug
  make
}

package() {
  cd "$srcdir/${_pkgname}-$pkgver"
  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
