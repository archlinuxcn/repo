# Maintainer: Stephan Springer <buzo+arch@Lini.de>
# Contributor: Maarten de Vries <maarten@de-vri.es>
# Based on AUR3 PKGBUILD by Ken Tossell <ken@tossell.net>

pkgname=libuvc
pkgver=0.0.7
pkgrel=3
pkgdesc="a cross-platform library for USB video devices"
arch=('i686' 'x86_64' 'aarch64')
url='https://libuvc.github.io/libuvc/'
license=('BSD-3-Clause')
depends=('glibc' 'libusb' 'libjpeg')
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::https://github.com/libuvc/libuvc/archive/v$pkgver.tar.gz")
sha256sums=('7c6ba79723ad5d0ccdfbe6cadcfbd03f9f75b701d7ba96631eb1fd929a86ee72')

options=(staticlibs)

build() {
    cmake -S libuvc-"$pkgver" -B build \
          -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
          -DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS" \
          -DCMAKE_INSTALL_PREFIX=/usr \
          -DCMAKE_INSTALL_LIBDIR=lib
    cmake --build build
}

package() {
    DESTDIR="${pkgdir}" cmake --install build
    install -DTm 644 "$srcdir/libuvc-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
