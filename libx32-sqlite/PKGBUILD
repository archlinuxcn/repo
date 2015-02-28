# $Id: PKGBUILD 126859 2015-01-31 15:00:35Z lcarlier $
# Maintainer: Biru Ionut <ionut@archlinux.ro>
# Contributor: Mikko Seppälä <t-r-a-y@mbnet.fi>
# Contributor: Kaos < gianlucaatlas dot gmail dot com >
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=sqlite
pkgname=libx32-sqlite
_amalgamationver=3080802
_docver=${_amalgamationver}
#_docver=3080401
pkgver=3.8.8.2
pkgrel=1.1
pkgdesc="A C library that implements an SQL database engine (x32 ABI)"
arch=('x86_64')
license=('custom')
url="http://www.sqlite.org/"
depends=(libx32-glibc $_pkgbasename)
makedepends=('tcl' 'gcc-multilib-x32' 'libx32-readline')
source=(http://www.sqlite.org/2015/sqlite-autoconf-${_amalgamationver}.tar.gz)
sha1sums=('1db237523419af7110e1d92c6b766e965f9322e4')
provides=("libx32-sqlite3=$pkgver")
replaces=("libx32-sqlite3")
conflicts=("libx32-sqlite3")

build() {
  cd ${srcdir}/sqlite-autoconf-${_amalgamationver}

  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  export LTLINK_EXTRAS="-ldl"
  export CFLAGS="$CFLAGS -DSQLITE_ENABLE_FTS3=1 -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_ENABLE_UNLOCK_NOTIFY -DSQLITE_SECURE_DELETE"

  ./configure --prefix=/usr --libdir=/usr/libx32 \
    --disable-static

  make
}


package() {
  cd ${srcdir}/sqlite-autoconf-${_amalgamationver}

  make DESTDIR=${pkgdir} install

  rm -rf "${pkgdir}"/usr/{include,share,bin}
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
