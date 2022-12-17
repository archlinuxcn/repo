# Maintainer: Torsten Keßler <tpkessler at archlinux dot org>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail dot com>

pkgname=rocm-device-libs
pkgver=5.4.1
pkgrel=1
pkgdesc='ROCm Device Libraries'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-Device-Libs'
license=('custom:NCSAOSL')
makedepends=('rocm-cmake' 'rocm-llvm')
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('cdb995d401707885402f2411f41eaa37593ada3f6d615cdbadce97e72d813b68')
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
