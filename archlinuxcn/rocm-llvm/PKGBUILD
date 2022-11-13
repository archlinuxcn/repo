# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-llvm
pkgdesc='Radeon Open Compute - LLVM toolchain (llvm, clang, lld)'
pkgver=5.3.2
pkgrel=2
arch=('x86_64')
url='https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.3/page/Overview_of_ROCmCC_Compiler.html'
license=('custom:Apache 2.0 with LLVM Exception')
makedepends=('cmake' 'python' 'ninja')
_git='https://github.com/RadeonOpenCompute/llvm-project'
source=("${pkgname}-${pkgver}.tar.gz::$_git/archive/rocm-$pkgver.tar.gz"
        "glibc2.36.patch")
sha256sums=('52c2822d3fccdfc124649c088640fcea537cd6f287162eb24c1de6d961b614d4'
            '8b667dd13cabedcdbc8cf2600d08f7a2b69d3f2a8a3b0e3b28c2f91ba3a61c50')
options=(staticlibs !lto)
_dirname="$(basename "$_git")-$(basename "${source[0]}" .tar.gz)"

prepare() {
    cd "$_dirname"
    # https://reviews.llvm.org/D129471
    patch -Np1 -i "$srcdir/glibc2.36.patch"
}

build() {
    cmake \
        -GNinja \
        -B build \
        -S "$_dirname/llvm" \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX='/opt/rocm/llvm' \
        -DLLVM_HOST_TRIPLE=$CHOST \
        -DLLVM_INSTALL_UTILS=ON \
        -DLLVM_ENABLE_BINDINGS=OFF \
        -DOCAMLFIND=NO \
        -DLLVM_ENABLE_OCAMLDOC=OFF \
        -DLLVM_INCLUDE_BENCHMARKS=OFF \
        -DLLVM_BUILD_TESTS=OFF \
        -DLLVM_ENABLE_PROJECTS='llvm;clang;compiler-rt;lld' \
        -DLLVM_TARGETS_TO_BUILD='AMDGPU;X86' \
        -DLLVM_BINUTILS_INCDIR=/usr/include
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build

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
