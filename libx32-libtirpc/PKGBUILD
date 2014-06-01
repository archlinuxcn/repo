# $Id$
# Upstream Maintainer: jtts
# Contributor: Tom Gundersen <teg@jklm.no>
# Contributor: Tobias Powalowski <tpowa@archlinux.org>
# Contributor: Franco Tortoriello <franco.tortoriello@gmail.com>
# Contributor: josephgbr <rafael.f.f1@gmail.com>
# Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libtirpc
pkgname=libx32-$_pkgbasename
pkgver=0.2.4
pkgrel=1
pkgdesc="Transport Independent RPC library (SunRPC replacement) (x32 ABI)"
arch=(x86_64)
url="http://libtirpc.sourceforge.net/"
license=(BSD)
depends=(libx32-krb5 $_pkgbasename)
makedepends=(gcc-multilib-x32)
#backup=('etc/netconfig')
source=(http://downloads.sourceforge.net/sourceforge/libtirpc/$_pkgbasename-$pkgver.tar.bz2)
sha256sums=('45c3e21dfc23a5ba501f9dfc6671678316fdfdb8355a1ec404ae2aa2f81943a1')

build() {
  cd "$srcdir/$_pkgbasename-$pkgver"

  ./configure --prefix=/usr --sysconf=/etc \
	--libdir=/usr/libx32 CC="gcc -mx32"

  make
}

package() {
  cd "$srcdir/$_pkgbasename-$pkgver"
  make DESTDIR="$pkgdir" install
  rm -rf "$pkgdir"/{etc,usr/{include,share}}
  install -dm755 "$pkgdir"/usr/share/licenses/
  ln -s $_pkgbasename "$pkgdir"/usr/share/licenses/$pkgname
}
