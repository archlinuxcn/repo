# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=comgr
pkgdesc='Compiler support library for ROCm LLVM'
pkgver=5.3.3
pkgrel=1
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/ROCm-CompilerSupport'
license=('custom:NCSAOSL')
depends=('rocm-device-libs')
makedepends=('rocm-cmake' 'rocm-llvm')
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('6a4ef69e672a077b5909977248445f0eedf5e124af9812993a4d444be030c78b')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
  cmake \
    -Wno-dev \
    -S "$_dirname/lib/comgr" \
    -B build \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DCMAKE_BUILD_TYPE=None \
    -DBUILD_TESTING=ON \
    -DCMAKE_PREFIX_PATH=/opt/rocm/llvm
  cmake --build build
}

check() {
    cmake --build build --target check-comgr
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  install -Dm644 "$_dirname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
