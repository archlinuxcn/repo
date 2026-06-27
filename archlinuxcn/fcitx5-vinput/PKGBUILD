# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Contributor: fcitx5-vinput maintainers <noreply@github.com>
# Contributor: xifan2333 <xifan233@163.com>

pkgname=fcitx5-vinput
pkgver=2.3.2
pkgrel=1
pkgdesc='Offline voice input addon for Fcitx5 with optional OpenAI-compatible postprocess'
arch=('x86_64')
url='https://github.com/xifan2333/fcitx5-vinput'
license=('GPL-3.0-only')
options=(!debug)
depends=('curl' 'fcitx5' 'libarchive' 'openssl' 'pipewire' 'qt6-base' 'sherpa-onnx')
makedepends=('clang' 'cli11' 'cmake' 'mold' 'ninja' 'nlohmann-json' 'pkgconf' 'qt6-tools')
source=("${url}/archive/v${pkgver}.tar.gz")
sha256sums=('0c0aca8362a4cc4660441e2065f43d0a39ed1103e5f90e84a41bac6bf90102bf')
provides=("${pkgname}")

build() {
    local src_root="${srcdir}/${pkgname}-${pkgver}"
    export CC=clang
    export CXX=clang++

    cmake -S "${src_root}" -B "${srcdir}/build" \
        -DCMAKE_BUILD_TYPE=None \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_EXE_LINKER_FLAGS=-fuse-ld=mold \
        -DCMAKE_SHARED_LINKER_FLAGS=-fuse-ld=mold \
        -DCMAKE_MODULE_LINKER_FLAGS=-fuse-ld=mold \
        -DVINPUT_PROJECT_VERSION="${pkgver}" \
        -DVINPUT_PACKAGE_RELEASE="${pkgrel}" \
        -DVINPUT_PACKAGE_HOMEPAGE_URL="${url}" \
        -DVINPUT_RUNTIME_MODE=system
    cmake --build "${srcdir}/build"
}

package() {
    DESTDIR="${pkgdir}" cmake --install "${srcdir}/build"
}
