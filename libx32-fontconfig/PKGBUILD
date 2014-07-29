# $Id: PKGBUILD 109875 2014-04-20 20:49:15Z bluewind $
# Maintainer: Jan de Groot <jgc@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=fontconfig
pkgname=libx32-$_pkgbasename
pkgver=2.11.1
pkgrel=1
pkgdesc="A library for configuring and customizing font access (x32 ABI)"
arch=(x86_64)
url="http://www.fontconfig.org/release/"
license=('custom')
depends=('libx32-expat' 'libx32-freetype2' $_pkgbasename)
makedepends=(gcc-multilib-x32)
options=('!libtool')
install=libx32-fontconfig.install
source=(http://www.fontconfig.org/release/${_pkgbasename}-${pkgver}.tar.bz2)
sha256sums=('dc62447533bca844463a3c3fd4083b57c90f18a70506e7a9f4936b5a1e516a99')

  # a nice page to test font matching:
  # http://zipcon.net/~swhite/docs/computers/browsers/fonttest.html

build() {
  cd $_pkgbasename-$pkgver

  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  # make sure there's no rpath trouble and sane .so versioning - FC and Gentoo do this as well
  libtoolize -f
  autoreconf -fi

  ./configure --prefix=/usr \
    --sysconfdir=/etc \
    --with-templatedir=/etc/fonts/conf.avail \
    --with-xmldir=/etc/fonts \
    --localstatedir=/var \
    --disable-static \
    --with-default-fonts=/usr/share/fonts \
    --with-add-fonts=/usr/share/fonts \
    --libdir=/usr/libx32
  make
}

check() {
  cd $_pkgbasename-$pkgver
  make -k check
}

package() {
  cd $_pkgbasename-$pkgver
  make DESTDIR="$pkgdir" install

  rm -rf "$pkgdir"/{etc,usr/{include,share}}
  find "$pkgdir/usr/bin" -not -type d -not -name fc-cache -delete
  mv "$pkgdir"/usr/bin/fc-cache{,-x32}

  # Install license
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
