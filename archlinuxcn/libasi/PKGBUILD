# Maintainer: Sebastian Baberowski <sebastian@baberowski.com>

pkgname=libasi
pkgver=1.8.7
pkgrel=1
pkgdesc="libasi used by INDI ASI drivers. Please note that for sake of simplicity package version is the version of libindi not a version of used ASI SDKs from ZWO. This package contains ASI Camera SDK, ASI EFW SDK, ASI EAF SDK and USBST4 SDK."
url="http://www.indilib.org/index.php?title=Main_Page"
license=(MIT)
arch=(i686 x86_64)
depends=(libindi=${pkgver})
makedepends=(cmake)
source=("https://github.com/indilib/indi-3rdparty/archive/v${pkgver}.tar.gz")
sha256sums=('7571bbc087e0efa2df992c174fca9a7e87e6b2a0f0c6d99cdff01af6fe7e82de')

prepare() {
  mkdir -p build
}

build() {
  cd build
  cmake -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DUDEVRULES_INSTALL_DIR=/usr/lib/udev/rules.d \
    ../indi-3rdparty-${pkgver}/libasi
  make
}


package() {
  cd build
  make DESTDIR="$pkgdir" install
}
