# $Id: PKGBUILD 249863 2015-10-30 14:00:49Z juergen $
# Maintainer: Dan McGee <dan@archlinux.org>
# Contributor: Manolis Tzanidakis <manolis@archlinux.org>

_pkgbasename=geoip
pkgname=libx32-geoip
pkgver=1.6.6
pkgrel=1.1
pkgdesc="Non-DNS IP-to-country resolver C library & utils (x32 ABI)"
arch=('x86_64')
url="http://www.maxmind.com/app/c"
license=('GPL')
depends=('libx32-zlib' 'geoip-database' "geoip")
makedepends=('autoconf' 'libtool')
options=('!emptydirs')
source=($_pkgbasename-$pkgver.tar.gz::https://github.com/maxmind/${_pkgbasename}-api-c/archive/v${pkgver}.tar.gz)
sha256sums=('db8ed5d07292c75cb3018738e6411037f15cc2a517f38ee04c1232cbe3d30b46')

prepare() {
  cd geoip-api-c-$pkgver
  autoreconf -vi
}

build() {
  cd geoip-api-c-$pkgver
	export CC="gcc -mx32"
	export CXX="g++ -mx32"
	export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  ./configure \
    --prefix=/usr \
		--libdir=/usr/libx32 \
    --mandir=/usr/share/man \
    --sysconfdir=/etc/geoip
  make
}

check() {
  cd geoip-api-c-$pkgver
  ln -sf /usr/share/GeoIP data
  make check
}

package() {
  cd geoip-api-c-$pkgver
  make DESTDIR="$pkgdir" install
	rm -rf "${pkgdir}"/usr/{include,share,bin}
	mkdir -p "$pkgdir/usr/share/licenses"
	ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}

# vim:set ts=2 sw=2 et:
