# Maintainer: Torsten Keßler <tpkessler at archlinux dot org>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-llvm
pkgdesc='Radeon Open Compute - LLVM toolchain (llvm, clang, lld)'
pkgver=5.4.1
pkgrel=1
arch=('x86_64')
url='https://docs.amd.com/bundle/ROCm-Compiler-Reference-Guide-v5.4/page/Introduction_to_Compiler_Reference_Guide.html'
license=('custom:Apache 2.0 with LLVM Exception')
makedepends=('cmake' 'python' 'ninja')
_git='https://github.com/RadeonOpenCompute/llvm-project'
source=("${pkgname}-${pkgver}.tar.gz::$_git/archive/rocm-$pkgver.tar.gz")
sha256sums=('909bdceef34814e83d29a71c668c72b04e832377e277a56895733d11e23822b3')
options=(staticlibs !lto)
_dirname="$(basename "$_git")-$(basename "${source[0]}" .tar.gz)"

build() {
    cmake \
        -GNinja \
        -B build \
        -S "$_dirname/llvm" \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX='/opt/rocm/llvm' \
        -DLLVM_HOST_TRIPLE=$CHOST \
        -DLLVM_ENABLE_PROJECTS='llvm;clang;compiler-rt;lld' \
        -DLLVM_TARGETS_TO_BUILD='AMDGPU;X86' \
        -DLLVM_INSTALL_UTILS=ON \
        -DLLVM_ENABLE_BINDINGS=OFF \
        -DLLVM_LINK_LLVM_DYLIB=OFF \
        -DLLVM_BUILD_LLVM_DYLIB=OFF \
        -DLLVM_LINK_LLVM_DYLIB=OFF \
        -DLLVM_ENABLE_ASSERTIONS=ON \
        -DOCAMLFIND=NO \
        -DLLVM_ENABLE_OCAMLDOC=OFF \
        -DLLVM_INCLUDE_BENCHMARKS=OFF \
        -DLLVM_BUILD_TESTS=ON \
        -DLLVM_INCLUDE_TESTS=ON \
        -DCLANG_INCLUDE_TESTS=ON \
        -DLLVM_BINUTILS_INCDIR=/usr/include
    cmake --build build
}

check() {
    LD_LIBRARY_PATH="$PWD/build/lib" \
    cmake --build build --target check-llvm{,-unit} check-clang{,-unit} check-lld
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
