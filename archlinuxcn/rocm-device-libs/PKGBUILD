# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail dot com>

pkgname=rocm-device-libs
pkgver=5.3.0
pkgrel=1
pkgdesc='ROCm Device Libraries'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-Device-Libs'
license=('custom:NCSAOSL')
makedepends=('rocm-cmake' 'rocm-llvm')
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('f7e1665a1650d3d0481bec68252e8a5e68adc2c867c63c570f6190a1d2fe735c')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
    cmake \
        -Wno-dev \
        -S "$_dirname" \
        -B build \
        -DCMAKE_C_COMPILER=/opt/rocm/llvm/bin/clang \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm \
        -DLLVM_DIR=/opt/rocm/llvm/lib/cmake/llvm
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 "$_dirname/LICENSE.TXT" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
