# $Id: PKGBUILD 144999 2015-10-26 07:27:19Z lcarlier $
# Maintainer: Biru Ionut <ionut@archlinux.ro>
# Contributor: Mikko Seppälä <t-r-a-y@mbnet.fi>
# Contributor: Kaos < gianlucaatlas dot gmail dot com >
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=sqlite
pkgname=libx32-sqlite
_srcver=3090100
_docver=${_srcver}
pkgver=3.9.1
pkgrel=1.1
pkgdesc="A C library that implements an SQL database engine (x32 ABI)"
arch=('x86_64')
license=('custom')
url="http://www.sqlite.org/"
depends=(libx32-glibc $_pkgbasename)
makedepends=('tcl' 'gcc-multilib-x32' 'libx32-readline')
source=(http://www.sqlite.org/2015/sqlite-src-${_srcver}.zip)
sha1sums=('7711364f78dae9110a7c8b62eba27c37aacb4205')
options=('!makeflags')
provides=("libx32-sqlite3=$pkgver")
replaces=("libx32-sqlite3")
conflicts=("libx32-sqlite3")

prepare() {
  cd "$srcdir"/sqlite-src-$_srcver
  autoreconf -vfi
}

build() {
  cd "$srcdir"/sqlite-src-$_srcver

  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  export LTLINK_EXTRAS="-ldl"
  export CFLAGS="$CFLAGS -DSQLITE_ENABLE_FTS3=1 \
                         -DSQLITE_ENABLE_COLUMN_METADATA=1 \
                         -DSQLITE_ENABLE_UNLOCK_NOTIFY \
                         -DSQLITE_ENABLE_DBSTAT_VTAB=1 \
                         -DSQLITE_ENABLE_RTREE=1 \
                         -DSQLITE_SECURE_DELETE"

  ./configure --prefix=/usr \
    --libdir=/usr/libx32 \
    --disable-tcl \
    --disable-static

  make
}

package() {
  cd "$srcdir"/sqlite-src-$_srcver

  make DESTDIR=${pkgdir} install

  rm -rf "${pkgdir}"/usr/{include,share,bin}
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
