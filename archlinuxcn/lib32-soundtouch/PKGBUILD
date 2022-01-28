# Maintainer: Nocifer <apmichalopoulos at gmail dot com>
# Contributor Maxime Gauduin <alucryd@archlinux.org>
# Contributor: josephgbr <rafael.f.f1@gmail.com>

pkgname='lib32-soundtouch'
pkgver=2.3.1
pkgrel=2
pkgdesc='An open-source audio processing library for changing the tempo, pitch and playback rates of audio streams or audio files (32 bit)'
arch=('x86_64')
url='https://www.surina.net/soundtouch'
license=('LGPL2.1')
depends=('lib32-gcc-libs' 'soundtouch')
makedepends=('cmake' 'git' 'ninja')
source=("${pkgname}-git::git+https://codeberg.org/soundtouch/soundtouch.git#tag=${pkgver}")
sha256sums=('SKIP')

build() {
    cd ${srcdir}

    cmake -S ${pkgname}-git -B build -G Ninja \
        -DCMAKE_BUILD_TYPE='Release' \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DBUILD_SHARED_LIBS=ON \
        -DCMAKE_CXX_FLAGS='-m32' \
        -DCMAKE_INSTALL_LIBDIR=lib32
    cmake --build build
}

package() {
    cd ${srcdir}

    DESTDIR="${pkgdir}" cmake --install build
    rm -rf "${pkgdir}"/usr/{bin,doc,include,share}
}
