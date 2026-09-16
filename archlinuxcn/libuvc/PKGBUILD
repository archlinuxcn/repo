# Maintainer: Stephan Springer <buzo+arch@Lini.de>
# Contributor: Maarten de Vries <maarten@de-vri.es>
# Based on AUR3 PKGBUILD by Ken Tossell <ken@tossell.net>

pkgname=libuvc
pkgver=0.0.8
pkgrel=1
pkgdesc="a cross-platform library for USB video devices"
arch=('i686' 'x86_64' 'aarch64')
url='https://libuvc.github.io/libuvc/'
license=('BSD-3-Clause')
depends=(glibc)
makedepends=(cmake libusb libjpeg-turbo)
source=("$pkgname-$pkgver.tar.gz::https://github.com/libuvc/libuvc/archive/v$pkgver.tar.gz")
sha256sums=('abe134716f4c53fe60db2004b42adf6af60e64e45808135acfa4311454371ece')

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
    depends+=(libusb libusb-1.0.so
              libjpeg-turbo libjpeg.so)
    DESTDIR="${pkgdir}" cmake --install build
    install -DTm 644 "$srcdir/libuvc-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
