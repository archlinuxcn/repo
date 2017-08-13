# $Id$
# Maintainer: PhotonX <photon89@googlemail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>

pkgname=libgnomeui
pkgver=2.24.5
pkgrel=2
pkgdesc="User Interface library for GNOME"
arch=('i686' 'x86_64')
license=('LGPL')
depends=('libbonoboui' 'libgnome-keyring' 'libsm')
makedepends=('intltool' 'pkg-config')
url="http://www.gnome.org"
source=(https://download.gnome.org/sources/$pkgname/2.24/$pkgname-$pkgver.tar.bz2)
sha256sums=('ae352f2495889e65524c979932c909f4629a58e64290fb0c95333373225d3c0f')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  ./configure --prefix=/usr --sysconfdir=/etc \
      --localstatedir=/var --disable-static \
      --libexecdir=/usr/lib/libgnomeui
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
}
