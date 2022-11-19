# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail dot com>

pkgname=rocm-device-libs
pkgver=5.3.3
pkgrel=1
pkgdesc='ROCm Device Libraries'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-Device-Libs'
license=('custom:NCSAOSL')
makedepends=('rocm-cmake' 'rocm-llvm')
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('963c9a0561111788b55a8c3b492e2a5737047914752376226c97a28122a4d768')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
    cmake \
        -Wno-dev \
        -S "$_dirname" \
        -B build \
        -DCMAKE_C_COMPILER=/opt/rocm/llvm/bin/clang \
        -DCMAKE_BUILD_TYPE=None \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DLLVM_DIR=/opt/rocm/llvm/lib/cmake/llvm
    cmake --build build
}

check() {
    cmake --build build --target test
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 "$_dirname/LICENSE.TXT" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
