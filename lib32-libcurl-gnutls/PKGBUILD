# Maintainer: Lizao (Larry) Li <lzlarryli gmail com>

pkgname=lib32-libcurl-gnutls
pkgver=7.48.0
pkgrel=0
pkgdesc='An URL retrieval utility and library'
arch=('x86_64')
url="http://curl.haxx.se"
license=(custom)
groups=()
depends=('lib32-libssh2' 'lib32-gnutls')
makedepends=('gcc-multilib')
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=('!libtool' '!strip')
source=("http://gentoo.osuosl.org/distfiles/curl-$pkgver.tar.bz2"
        "http://curl.haxx.se/download/curl-$pkgver.tar.bz2.asc")
md5sums=('d42e0fc34a5cace5739631cc040974fe'
         'SKIP')
validpgpkeys=('914C533DF9B2ADA2204F586D78E11C6B279D5C91') # Daniel Stenberg

build() {
  cd "curl-$pkgver"
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
  ./configure \
      --libdir=/usr/lib32 \
      --prefix=/usr \
      --mandir=/usr/share/man \
      --disable-dependency-tracking \
      --enable-versioned-symbols \
      --disable-ldap \
      --disable-ldaps \
      --enable-ipv6 \
      --enable-manual \
      --enable-threaded-resolver \
      --without-libidn \
      --with-random=/dev/urandom \
      --with-ca-bundle=/etc/ssl/certs/ca-certificates.crt \
      --without-ssl \
      --with-gnutls=/usr
  make
}

package() {
  install -Dm644 $srcdir/curl-$pkgver/lib/.libs/libcurl.so.4.4.0 $pkgdir/usr/lib32/libcurl-gnutls.so.4.4.0
  ln -s libcurl-gnutls.so.4.4.0 $pkgdir/usr/lib32/libcurl-gnutls.so.4
  install -Dm644 $srcdir/curl-$pkgver/docs/LICENSE-MIXING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
