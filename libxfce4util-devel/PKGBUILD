# $Id: PKGBUILD 198279 2013-10-30 13:54:02Z allan $
# Maintainer: Evangelos Foutras <evangelos@foutrelis.com>
# Contributor: tobias <tobias funnychar archlinux.org>

_pkgname=libxfce4util
pkgname=${_pkgname}-devel
pkgver=4.11.0
pkgrel=1
pkgdesc="Basic utility non-GUI functions for Xfce"
arch=('i686' 'x86_64')
url="http://www.xfce.org/"
license=('GPL2')
depends=('glib2')
provides=("${_pkgname}=${pkgver}")
conflicts=("${_pkgname}")
makedepends=('pkgconfig' 'intltool' 'gtk-doc')
source=(http://archive.xfce.org/src/xfce/${_pkgname}/4.11/${_pkgname}-$pkgver.tar.bz2)
sha256sums=('d75a7f80c4b107d927926e9d61a31605d54e62bec2939f39dc59d8eaabc0005a')

build() {
  cd "$srcdir/${_pkgname}-$pkgver"

  ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --sbindir=/usr/bin \
    --libexecdir=/usr/lib \
    --localstatedir=/var \
    --disable-static \
    --enable-gtk-doc \
    --disable-debug
  make
}

package() {
  cd "$srcdir/${_pkgname}-$pkgver"
  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
