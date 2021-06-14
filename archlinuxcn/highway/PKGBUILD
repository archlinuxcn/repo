# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgname=highway
pkgver=0.12.2
pkgrel=1
pkgdesc='A C++ library for SIMD (Single Instruction, Multiple Data)'
arch=('x86_64')
url='https://github.com/google/highway/'
license=('Apache')
makedepends=('cmake' 'gtest' 'gmock')
source=("https://github.com/google/highway/archive/${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('e1d47ce510429fdcf31f41697ca74fb0dcd59d933196e531a86d51751a56f4cc')

build() {
    export CXXFLAGS+=' -DHWY_COMPILE_ALL_ATTAINABLE'
    cmake -B build -S "${pkgname}-${pkgver}" \
        -DCMAKE_BUILD_TYPE:STRING='None' \
        -DCMAKE_INSTALL_PREFIX:PATH='/usr' \
        -DHWY_SYSTEM_GTEST:BOOL='ON' \
        -Wno-dev
    make -C build
}

check() {
    make -C build test
}

package() {
    make -C build DESTDIR="$pkgdir" install
}
