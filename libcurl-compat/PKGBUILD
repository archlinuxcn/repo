# Maintainer: Evan Anderson <evananderson@thelinuxman.us>
# Contributor: Christian Hesse <arch@eworm.de>
# Contributor: PitBall

pkgname=libcurl-compat
_pkgname=curl
pkgver=7.49.1
pkgrel=1
pkgdesc="An URL retrieval library (without versioned symbols)"
arch=('i686' 'x86_64')
url="http://curl.haxx.se"
license=('MIT')
depends=('ca-certificates' 'gnutls' 'openssl' 'zlib' 'libidn' 'libssh2' 'krb5')
options=('strip')
#conflicts=('libcurl-gnutls')
source=("http://curl.haxx.se/download/${_pkgname}-$pkgver.tar.gz")
md5sums=('2feb3767b958add6a177c6602ff21e8c')
install=libcurl-compat.install

build() {
  config="./configure \
      --prefix=/usr \
      --disable-ldap \
      --disable-ldaps \
      --enable-ipv6 \
      --disable-manual \
      --disable-versioned-symbols \
      --enable-threaded-resolver \
      --with-gssapi \
      --with-libidn \
      --with-random=/dev/urandom \
      --with-ca-bundle=/etc/ssl/certs/ca-certificates.crt"

  #cp -a ${_pkgname}-$pkgver{,-gnutls}

  #cd "${_pkgname}-$pkgver-gnutls"
  #$config --with-ssl --with-gnutls
  #make -C lib

  cd ${_pkgname}-$pkgver
  $config
  make -C lib
}

package() {
  #cd "${_pkgname}-$pkgver-gnutls"
  #make -C lib DESTDIR="$pkgdir" install
  #mv $pkgdir/usr/lib/libcurl.so.4.4.0 \
  #  $pkgdir/usr/lib/libcurl-gnutls-compat.so.4.4.0
  cd ${_pkgname}-$pkgver
  make -C lib DESTDIR="$pkgdir" install
  mv $pkgdir/usr/lib/libcurl.so.4.4.0 \
    $pkgdir/usr/lib/libcurl-compat.so.4.4.0
  rm $pkgdir/usr/lib/libcurl.so{,.4}
  rm -rf $pkgdir/etc
  ln -s libcurl-compat.so.4.4.0  $pkgdir/usr/lib/libcurl.so.3
  ln -s libcurl-compat.so.4.4.0  $pkgdir/usr/lib/libcurl.so.4.0.0
  ln -s libcurl-compat.so.4.4.0  $pkgdir/usr/lib/libcurl.so.4.1.0
  ln -s libcurl-compat.so.4.4.0  $pkgdir/usr/lib/libcurl.so.4.2.0
  ln -s libcurl-compat.so.4.4.0  $pkgdir/usr/lib/libcurl.so.4.3.0
  #ln -s libcurl-gnutls-compat.so.4.4.0  $pkgdir/usr/lib/libcurl-gnutls.so.3

  # license
  install -d "$pkgdir/usr/share/licenses"
  ln -s "$_pkgname" "$pkgdir/usr/share/licenses/$pkgname"
}
