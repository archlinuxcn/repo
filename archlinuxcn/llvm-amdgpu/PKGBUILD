# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=llvm-amdgpu
pkgdesc='Radeon Open Compute - LLVM toolchain (llvm, clang, lld)'
pkgver=4.2.0
pkgrel=2
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/llvm-project'
license=('custom:Apache 2.0 with LLVM Exception')
depends=(z3)
makedepends=(cmake python ninja)
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/rocm-$pkgver.tar.gz"
        "libstdc++-11.1.0-workaround.patch::https://reviews.llvm.org/file/data/77rbtfy27xsj2sgfygq5/PHID-FILE-7vya6mqfpldq7sohw56a/file")
sha256sums=('751eca1d18595b565cfafa01c3cb43efb9107874865a60c80d6760ba83edb661'
            'c874456a8a616735bf524772f7ca229d8e59d9775b2b5f19d734df1afda57d11')
options=(staticlibs)
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

prepare() {
    cd "$_dirname"

    # fix compatibility with GCC 11: https://github.com/ROCmSoftwarePlatform/rocBLAS/issues/1191#issuecomment-851634017
    patch -Np1 < "$srcdir/libstdc++-11.1.0-workaround.patch"
}

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
