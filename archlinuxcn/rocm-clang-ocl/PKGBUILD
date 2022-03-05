# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Lucas Magalhães <whoisroot@national.shitposting.agency>
pkgname=rocm-clang-ocl
pkgver=5.0.2
pkgrel=1
pkgdesc="OpenCL compilation with clang compiler."
arch=('x86_64')
url="https://github.com/RadeonOpenCompute/clang-ocl"
license=('unknown')
depends=('rocm-llvm' 'rocm-opencl-runtime')
makedepends=('cmake' 'rocm-cmake')
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('5e8f39200227388817024ee7ce46a996e43e433ed308f8d5e8e4c03629d8a5e7')
_dirname="$(basename "$url")-$(basename ${source[0]} .tar.gz)"

build() {
  cmake -Wno-dev -B build \
        -S "$_dirname" \
        -DCLANG_BIN=/opt/rocm/llvm/bin \
        -DBITCODE_DIR=/opt/rocm/amdgcn/bitcode \
        -DCMAKE_INSTALL_PREFIX=/opt/rocm

  make -C build
}

check() {
  make -C build check
}

package() {
  DESTDIR="$pkgdir" make -C build install
}
