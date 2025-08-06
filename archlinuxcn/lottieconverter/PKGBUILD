# Contributor: BluePeril <blueperil (at) blueperil _dot_ de>

_pkgname=lottieconverter
pkgname=lottieconverter
pkgver=0.2
pkgrel=3
pkgdesc='Simple, dummy lottie converter'
arch=('x86_64')
url='https://github.com/sot-tech/LottieConverter'
license=('LGPL-v2.1')
makedepends=('git' 'cmake')
depends=('rlottie' 'libpng' 'giflib')
provides=(${_pkgname})
source=(${_pkgname}::"git+https://github.com/sot-tech/LottieConverter.git#tag=r${pkgver}")
sha256sums=('21acf3b34c7ba5763f8c838e80778a9baa41950116c08e9a63f49eb6fd7a3d59')

prepare() {
    cd "${_pkgname}"
    mkdir build
}

build() {
    cd "${_pkgname}/build"

    cmake -DCMAKE_BUILD_TYPE=Release -DSYSTEM_RL=true -DSYSTEM_GL=true ..
    cmake --build .
}

package() {
    cd "${_pkgname}/build"

    install -d -m755 "${pkgdir}/usr/bin"
    install -D -m755 lottieconverter "${pkgdir}/usr/bin/lottieconverter"
}

