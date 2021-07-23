# Maintainer: Zion Nimchuk <zionnimchuk@gmail.com>
# Contributor: Lex Black <autumn-wind@web.de>
# Contributor: Maxime Vincent <maxime.vince@gmail.com>
# Contributor: Gustavo Alvarez <sl1pkn07@gmail.com>

pkgname=wolfssl
pkgver=4.8.1
pkgrel=1
pkgdesc='small, fast, portable implementation of TLS/SSL for embedded devices to the cloud (formerly CyaSSL)'
arch=(i686 x86_64)
license=(GPL)
depends=('sh')
makedepends=('cmake')
url='https://www.wolfssl.com/'
source=(${pkgname}-${pkgver}-stable.tar.gz::https://github.com/wolfSSL/wolfssl/archive/v$pkgver-stable.tar.gz
        https://github.com/wolfSSL/wolfssl/releases/download/v${pkgver}-stable/${pkgname}-${pkgver}-stable.tar.gz.asc)
sha256sums=('50db45f348f47e00c93dd244c24108220120cb3cc9d01434789229c32937c444'
            'SKIP')
validpgpkeys=('A2A48E7BCB96C5BECB987314EBC80E415CA29677')

prepare() {
  mkdir -p build-$pkgver
}

build() {
  cd build-$pkgver
  cmake ../$pkgname-$pkgver-stable \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=ON \
    -DWOLFSSL_EXAMPLES=no \
    -DWOLFSSL_FAST_MATH=no \
    -DWOLFSSL_CRYPT_TESTS=no \
    -DWOLFSSL_REPRODUCIBLE_BUILD=yes \
    -DWOLFSSL_CURVE25519=yes \
    -DWOLFSSL_ED25519=yes \
    -DWOLFSSL_CURVE448=yes \
    -DWOLFSSL_ED448=yes
  make
    
  # Run make using Makefiles so that we also provide the regular pkg-config files
  cd ../$pkgname-$pkgver-stable
  ./autogen.sh
  ./configure --prefix=/usr --sysconfdir=/etc --disable-fastmath \
              --disable-fasthugemath \
              --disable-bump \
              --enable-opensslextra \
              --enable-fortress \
              --enable-keygen \
              --enable-certgen \
              --disable-debug \
              --disable-ntru \
              --disable-examples \
              --enable-distro \
              --enable-reproducible-build \
              --enable-curve25519 \
              --enable-ed25519 \
              --enable-curve448 \
              --enable-ed448
  make
}

package() {
  make -C build-$pkgver install DESTDIR="$pkgdir"
  cd $pkgname-$pkgver-stable
  make install DESTDIR="$pkgdir"
  install -Dm644 COPYING "$pkgdir"/usr/share/licenses/$pkgname/COPYING
  libtool --finish /usr/lib
}
