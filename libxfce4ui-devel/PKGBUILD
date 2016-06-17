# Maintainer: twa022 <twa022 at gmail dot com>

_pkgname=libxfce4ui
pkgname=${_pkgname}-devel
pkgver=4.13.0
pkgrel=1
pkgdesc="Commonly used Xfce widgets among Xfce applications"
arch=('i686' 'x86_64')
url="http://www.xfce.org/"
license=('GPL2')
depends=('libxfce4util' 'gtk2' 'xfconf' 'libsm' 'startup-notification'
         'hicolor-icon-theme' 'gtk3')
makedepends=('intltool' 'gtk-doc')
provides=("${_pkgname}=${pkgver}")
conflicts=("${_pkgname}")
#replaces=('libxfcegui4') - later when all is ported
options=('!libtool')
source=(http://archive.xfce.org/src/xfce/$_pkgname/${pkgver%.*}/$_pkgname-$pkgver.tar.bz2)

build() {
  cd "$srcdir/$_pkgname-$pkgver"

  ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --libexecdir=/usr/lib \
    --localstatedir=/var \
    --disable-static \
    --enable-gtk-doc \
    --disable-debug \
    --with-vendor-info='Arch Linux'
  make
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
}

sha256sums=('22f0b66a33945f347952249589f71618418f1e47ca847850eb0ee1bdb0c353d4')
