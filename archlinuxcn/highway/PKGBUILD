# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgname=highway
pkgver=0.14.2
pkgrel=1
pkgdesc='A C++ library for SIMD (Single Instruction, Multiple Data)'
arch=('x86_64')
url='https://github.com/google/highway/'
license=('Apache')
makedepends=('cmake' 'gtest' 'gmock')
source=("https://github.com/google/highway/archive/${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('58f7f3a12394341796fbb3045d18020474cb214ef85b9a50bbaaa809e34e9232')

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
