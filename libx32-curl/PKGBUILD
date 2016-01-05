# $Id: PKGBUILD 153571 2015-12-17 12:44:34Z fyan $
# Maintainer: Daniel Wallace <danielwallace@aur.archlinux.org>
# Contributor: Dave Reisner <dreisner@archlinux.org>
# Contributor: Angel Velasquez <angvp@archlinux.org>
# Contributor: Eric Belanger <eric@archlinux.org>
# Contributor: Lucien Immink <l.immink@student.fnt.hvu.nl>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

pkgname=libx32-curl
_pkgname=curl
pkgver=7.46.0
pkgrel=1.1
pkgdesc="An URL retrieval utility and library (x32 ABI)"
arch=('x86_64')
url="http://curl.haxx.se"
license=('MIT')
depends=('libx32-libssh2' 'libx32-krb5' 'libx32-libidn' "${_pkgname}")
source=("http://curl.haxx.se/download/$_pkgname-$pkgver.tar.gz"{,.asc}
        curlbuild-stub.h)
md5sums=('230e682d59bf8ab6eca36da1d39ebd75'
         'SKIP'
         'f8006c96c36ab7049412350968eb0389')
 validpgpkeys=('914C533DF9B2ADA2204F586D78E11C6B279D5C91') # Daniel Stenberg

build() {
  cd "$_pkgname-$pkgver"

  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"
  
  ./configure \
      --prefix=/usr \
      --mandir=/usr/share/man \
      --disable-dependency-tracking \
      --disable-ldap \
      --disable-ldaps \
      --enable-ipv6 \
      --enable-manual \
      --enable-versioned-symbols \
      --enable-threaded-resolver \
      --with-gssapi \
      --with-libidn \
      --with-random=/dev/urandom \
      --with-ca-bundle=/etc/ssl/certs/ca-certificates.crt \
      --libdir=/usr/libx32

  make
}

package() {
  install="${pkgname}.install"

  cd "$_pkgname-$pkgver"

  make DESTDIR="$pkgdir" install

  rm -rf "${pkgdir}"/usr/{share,bin}
  
  # license
  install -d "$pkgdir/usr/share/licenses"
  ln -s "$_pkgname" "$pkgdir/usr/share/licenses/$pkgname"

  # devel
  find "${pkgdir}/usr/include/curl" -type f -not -name curlbuild.h -delete
  install -Dm644 "${srcdir}/curlbuild-stub.h" "${pkgdir}/usr/include/_$pkgname/curlbuild-stub.h"
  mv "$pkgdir/usr/include/curl/curlbuild.h" "$pkgdir/usr/include/$_pkgname/curlbuild-x32.h"
}
