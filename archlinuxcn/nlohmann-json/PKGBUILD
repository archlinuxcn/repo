# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=nlohmann-json
pkgver=3.7.3
pkgrel=2
pkgdesc="Header-only JSON library for Modern C++"
url="https://github.com/nlohmann/json"
license=('MIT')
arch=('any') # check function needs a working compiler toolchain, but package really is arch independent 
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('249548f4867417d66ae46b338dfe0a2805f3323e81c9e9b83c89f3adbfde6f31')

build() {
    cd json-$pkgver
    
    cmake "$srcdir"/json-$pkgver \
        -DBUILD_TESTING=ON \
        -DCMAKE_INSTALL_PREFIX=/usr \
	-DCMAKE_INSTALL_LIBDIR=/usr/lib \
	-DJSON_MultipleHeaders=ON
    make
}

package() {
    cd json-$pkgver
    make DESTDIR="$pkgdir" install
    install -Dm644 "$srcdir"/json-$pkgver/LICENSE.MIT "$pkgdir"/usr/share/licenses/$pkgname/LICENSE.MIT
}
