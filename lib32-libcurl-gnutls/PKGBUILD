# Maintainer: Lizao (Larry) Li <lzlarryli gmail com>

pkgname=lib32-libcurl-gnutls
pkgver=7.50.1
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
source=("https://curl.haxx.se/download/curl-$pkgver.tar.bz2"
        "http://curl.haxx.se/download/curl-$pkgver.tar.bz2.asc")
md5sums=('015f6a0217ca6f2c5442ca406476920b'
         'SKIP')
validpgpkeys=('27EDEAF22F3ABCEB50DB9A125CC908FDB71E12C2') # Daniel Stenberg 2016

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
