# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Lucas Magalhães <whoisroot@national.shitposting.agency>
pkgname=rocm-clang-ocl
pkgver=5.2.1
pkgrel=1
pkgdesc="OpenCL compilation with clang compiler."
arch=('x86_64')
url="https://github.com/RadeonOpenCompute/clang-ocl"
license=('unknown')
depends=('rocm-llvm' 'rocm-opencl-runtime')
makedepends=('cmake' 'rocm-cmake')
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('693a9a360cb2f7e6910a6714df236df6a9d984f94b01712103a520d8e506c03f')
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
