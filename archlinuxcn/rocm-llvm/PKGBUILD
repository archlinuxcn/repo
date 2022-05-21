# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-llvm
pkgdesc='Radeon Open Compute - LLVM toolchain (llvm, clang, lld)'
pkgver=5.1.3
pkgrel=1
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/llvm-project'
license=('custom:Apache 2.0 with LLVM Exception')
depends=(z3)
makedepends=(cmake python ninja)
provides=("llvm-amdgpu")
replaces=('llvm-amdgpu')
conflicts=('llvm-amdgpu')
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('d236a2064363c0278f7ba1bb2ff1545ee4c52278c50640e8bb2b9cfef8a2f128')
options=(staticlibs !lto)
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

# NINJAFLAGS is an env var used to pass commandline options to ninja
# NOTE: It's your responbility to validate the value of $NINJAFLAGS. If unsure, don't set it.
# NINJAFLAGS="-j20"

build() {
    cmake -GNinja -S "$_dirname/llvm" \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX='/opt/rocm/llvm' \
        -DLLVM_HOST_TRIPLE=$CHOST \
        -DLLVM_BUILD_UTILS=ON \
        -DLLVM_ENABLE_BINDINGS=OFF \
        -DOCAMLFIND=NO \
        -DLLVM_ENABLE_OCAMLDOC=OFF \
        -DLLVM_INCLUDE_BENCHMARKS=OFF \
        -DLLVM_BUILD_TESTS=OFF \
        -DLLVM_ENABLE_PROJECTS='llvm;clang;compiler-rt;lld' \
        -DLLVM_TARGETS_TO_BUILD='AMDGPU;X86' \
        -DLLVM_BINUTILS_INCDIR=/usr/include
    ninja $NINJAFLAGS
}

package() {
    DESTDIR="$pkgdir" ninja $NINJAFLAGS install

    # https://bugs.archlinux.org/task/28479
    install -d "$pkgdir/opt/rocm/llvm/lib/bfd-plugins"
    ln -s /opt/rocm/llvm/lib/LLVMgold.so "$pkgdir/opt/rocm/llvm/lib/bfd-plugins/LLVMgold.so"

    cd "$_dirname"
    install -Dm644 llvm/LICENSE.TXT "$pkgdir/usr/share/licenses/$pkgname/llvm-LICENSE"
    install -Dm644 clang/LICENSE.TXT "$pkgdir/usr/share/licenses/$pkgname/clang-LICENSE"
    install -Dm644 clang-tools-extra/LICENSE.TXT "$pkgdir/usr/share/licenses/$pkgname/clang-tools-extra-LICENSE"
    install -Dm644 compiler-rt/LICENSE.TXT "$pkgdir/usr/share/licenses/$pkgname/compiler-rt-LICENSE"
    install -Dm644 lld/LICENSE.TXT "$pkgdir/usr/share/licenses/$pkgname/lld-LICENSE"
}
