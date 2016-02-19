# based on official curl package
# Maintainer: Jose Riha <jose1711 gmail com>

pkgname=libcurl-gnutls
_pkgname=curl
pkgver=7.47.0
pkgrel=1
pkgdesc="An URL retrieval utility and library"
arch=('i686' 'x86_64')
url="http://curl.haxx.se"
license=('MIT')
depends=('ca-certificates' 'libssh2' 'zlib' 'gnutls')
options=('!libtool' '!strip')
source=("http://curl.haxx.se/download/$_pkgname-$pkgver.tar.gz"
        curlbuild.h
        01_runtests_gdb.patch
        02_art_http_scripting.patch
        03_keep_symbols_compat.patch
        04_workaround_as_needed_bug.patch
        06_always-disable-valgrind.patch
        07_do-not-disable-debug-symbols.patch
        90_gnutls.patch
        99_nss.patch)

md5sums=('5109d1232d208dfd712c0272b8360393'
         '751bd433ede935c8fae727377625a8ae'
         'e6b1f326a81f4a21e829f0a7ce43619f'
         '5cadcf82367cef12738fc3b0ef27483f'
         '955b12e575215735b6bd563ee2e3af2a'
         'fd110c854e055d0375798c2857bd260e'
         '2cc79bcb4c64e131f4be9f86a5d7f2cb'
         'eb393f4dcd524916372c6bdd66c78c0b'
         '8647154bd1e6943b072afad746e8fc9b'
         '92089fe6b6e4f57fe109db89c6a643ce')

ptrsize=$(cpp <<<'__SIZEOF_POINTER__' | sed '/^#/d')
case $ptrsize in
  8) _curlbuild=curlbuild-64.h ;;
  4) _curlbuild=curlbuild-32.h ;;
  *) error "unknown pointer size for architecture: %s bytes" "$ptrsize"
    exit 1
    ;;
esac

build() {
  cd "$_pkgname-$pkgver"
  # apply debian patches
  for i in ../*patch
	do
	echo "using $i"
	patch -p1 < "$i"
	done

  ./configure \
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
  install -Dm644 $srcdir/$_pkgname-$pkgver/lib/.libs/libcurl.so.4.4.0 $pkgdir/usr/lib/libcurl-gnutls.so.4.4.0
  ln -s libcurl-gnutls.so.4.4.0 $pkgdir/usr/lib/libcurl-gnutls.so.4
  ln -s libcurl-gnutls.so.4.4.0 $pkgdir/usr/lib/libcurl-gnutls.so.3
}
