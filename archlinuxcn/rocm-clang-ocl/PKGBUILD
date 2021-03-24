# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Lucas Magalhães <whoisroot@national.shitposting.agency>
pkgname=rocm-clang-ocl
pkgver=4.1.0
pkgrel=1
pkgdesc="OpenCL compilation with clang compiler."
arch=('x86_64')
url="https://github.com/RadeonOpenCompute/clang-ocl"
license=('unknown')
depends=('llvm-amdgpu' 'rocm-opencl-runtime')
makedepends=('cmake' 'rocm-cmake')
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('c6e65da5541df9ee940caeeffe1b87c92547edc1770538fd2010c9c998a593b5')
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
