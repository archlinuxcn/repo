# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-llvm
pkgdesc='Radeon Open Compute - LLVM toolchain (llvm, clang, lld)'
pkgver=5.0.0
pkgrel=1
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/llvm-project'
license=('custom:Apache 2.0 with LLVM Exception')
depends=(z3)
makedepends=(cmake clang python ninja)
provides=("llvm-amdgpu")
replaces=('llvm-amdgpu')
conflicts=('llvm-amdgpu')
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('bca2db4aaab71541cac588d6a708fde60f0ebe744809bde8a3847044a1a77413')
options=(staticlibs)
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
    CC=/usr/bin/clang \
    CXX=/usr/bin/clang++ \
    cmake -GNinja \
        -Wno-dev \
        -S "$_dirname/llvm" \
        -DCMAKE_INSTALL_PREFIX='/opt/rocm/llvm' \
        -DCMAKE_BUILD_TYPE=Release \
        -DLLVM_HOST_TRIPLE=$CHOST \
        -DLLVM_BUILD_UTILS=ON \
        -DLLVM_ENABLE_BINDINGS=OFF \
        -DLLVM_ENABLE_OCAMLDOC=OFF \
        -DLLVM_ENABLE_PROJECTS='llvm;clang;compiler-rt;lld' \
        -DLLVM_TARGETS_TO_BUILD='AMDGPU;X86' \
        -DOCAMLFIND=NO
    ninja
}

package() {
    DESTDIR="$pkgdir" ninja install
}
