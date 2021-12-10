# Maintainer: DuckSoft <realducksoft@gmail.com>
pkgname=across
_pkgname=ACross
pkgver=0.1.1
pkgrel=1
pkgdesc="The next GUI client for v2ray core"
arch=('x86_64')
url='https://github.com/ArkToria/ACross'
license=('GPL3')
depends=('hicolor-icon-theme' 'qt6-base' 'qt6-svg' 'qt6-quickcontrols2' 'qt6-translations'
    'qt6-tools' 'qt6-imageformats' 'qt6-5compat' 'curl' 'fmt' 'grpc'
    'nlohmann-json' 'protobuf' 'spdlog' 'zxing-cpp' 'clang')
makedepends=('git' 'cmake' 'clang' 'ninja' 'gcc' 'gtest')
optdepends=('v2ray: use system v2ray core.'
    'noto-fonts: default display fonts')
provides=('across')

source=("across-${pkgver}.tar.gz::https://github.com/ArkToria/ACross/archive/refs/tags/v${pkgver}.tar.gz")

sha256sums=('7477ab8a9551373d4f0d237856a4730c4c8854304df1f041afe1d64b0a14b924')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}/"

    mkdir -p build && cd build
    cmake .. \
        -DCMAKE_INSTALL_PREFIX=${pkgdir}/usr \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_INFO="Arch Linux - ${pkgver}" \
        -GNinja
    ninja
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    ninja -C "build" install
}
