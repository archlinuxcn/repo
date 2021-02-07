# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgname=highway
pkgver=0.7.0
pkgrel=1
pkgdesc='A C++ library for SIMD (Single Instruction, Multiple Data)'
arch=('x86_64')
url='https://github.com/google/highway/'
license=('Apache')
makedepends=('cmake' 'gtest')
source=("https://github.com/google/highway/archive/v${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('f76535f236f77716453d5eca6ba4941ac7bbfb8f6306400f4dcf87fbf7ba3989')

build() {
    cmake -B build -S "${pkgname}-${pkgver}" \
        -DCMAKE_BUILD_TYPE:STRING='None' \
        -DCMAKE_INSTALL_PREFIX:PATH='/usr' \
        -DHWY_SYSTEM_GTEST:BOOL='ON' \
        -DCMAKE_CXX_FLAGS:STRING="${CXXFLAGS} -DHWY_COMPILE_ALL_ATTAINABLE" \
        -Wno-dev
    make -C build
}

check() {
    make -C build test
}

package() {
    make -C build DESTDIR="$pkgdir" install
}
