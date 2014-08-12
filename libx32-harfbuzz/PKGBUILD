# Maintainer: Florian Pritz <bluewind@xinu.at>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=harfbuzz
pkgname=libx32-$_pkgbasename
pkgver=0.9.32
pkgrel=1
pkgdesc="OpenType text shaping engine. (x32 ABI)"
arch=('x86_64')
url="http://www.freedesktop.org/wiki/Software/HarfBuzz"
license=('MIT')
depends=('libx32-icu' 'libx32-glib2' 'libx32-freetype2' $_pkgbasename)
makedepends=('gcc-multilib-x32')
source=(http://www.freedesktop.org/software/harfbuzz/release/${_pkgbasename}-${pkgver}.tar.bz2)
sha256sums=('430c81744e2d87b36f529b16f18efd0d0140aee9df59b2ee312f5de1994b9db4')

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd "${srcdir}/${_pkgbasename}-${pkgver}"

  # work around autogen.sh requiring ragel
  autoreconf --force --install --verbose
  ./configure --prefix=/usr --libdir=/usr/libx32 --disable-silent-rules --with-graphite2=no --without-cairo
  make
}

package() {
  cd "${srcdir}/${_pkgbasename}-${pkgver}"

  make DESTDIR="${pkgdir}" install

  rm -rf "${pkgdir}"/usr/{include,share,bin}
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
