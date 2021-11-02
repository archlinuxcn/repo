# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=llvm-amdgpu
pkgdesc='Radeon Open Compute - LLVM toolchain (llvm, clang, lld)'
pkgver=4.5.0
pkgrel=1
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/llvm-project'
license=('custom:Apache 2.0 with LLVM Exception')
depends=(z3)
makedepends=(cmake python ninja)
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('e33d08c8ae42a3ba394dceb8938263cd14ba45e9603b18f3502c3344814ca296')
options=(staticlibs)
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

build() {
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
