# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgname=highway
pkgver=0.14.1
pkgrel=1
pkgdesc='A C++ library for SIMD (Single Instruction, Multiple Data)'
arch=('x86_64')
url='https://github.com/google/highway/'
license=('Apache')
makedepends=('cmake' 'gtest' 'gmock')
source=("https://github.com/google/highway/archive/${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('4407b83f2e5b1e696d1f80da8179a55ef64716dadde18102f04ad60cfd2d5898')

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
