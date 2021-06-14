# Maintainer: archibald869 <archibald869 at web dot de>

pkgname=cling
pkgver=0.9
pkgrel=1
pkgdesc="Interactive C++ interpreter, built on the top of LLVM and Clang libraries"
arch=("i686" "x86_64")
url="https://root.cern.ch/cling"
license=("custom:Cling Release License")
provides=("cling")
conflicts=("cling")
depends=("libxml2")
makedepends=("git" "cmake" "python2")
optdepends=(
    "python2: support for scan-view and Jupyter"
    "perl: support for scan-build, ccc-analyzer and c++-analyzer"
)
source=(
    "llvm::git+http://root.cern/git/llvm.git#branch=cling-patches"
    "clang::git+http://root.cern/git/clang.git#branch=cling-patches"
    "cling::git+http://root.cern/git/cling.git#tag=v$pkgver"
)
sha256sums=(
    "SKIP"
    "SKIP"
    "SKIP"
)


prepare() {
    if [ ! -h "$srcdir/llvm/tools/clang" ]; then
        ln -s "$srcdir/clang" "$srcdir/llvm/tools/clang"
    fi

    if [ ! -h "$srcdir/llvm/tools/cling" ]; then
        ln -s "$srcdir/cling" "$srcdir/llvm/tools/cling"
    fi

    # patch missing header file
    sed -i '/^#include <vector>$/i #include <limits>' \
        "$srcdir/llvm/utils/benchmark/src/benchmark_register.h"
}

build() {
    mkdir -p "$srcdir/build"
    cd "$srcdir/build"

    cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX="/opt/cling" \
        -DLLVM_TARGETS_TO_BUILD="host;NVPTX" \
        -DLLVM_BUILD_LLVM_DYLIB=OFF \
        -DLLVM_ENABLE_RTTI=ON \
        -DLLVM_ENABLE_FFI=ON \
        -DLLVM_BUILD_DOCS=OFF \
        -DLLVM_BUILD_TOOLS=OFF \
        -DLLVM_ENABLE_SPHINX=OFF \
        -DLLVM_ENABLE_DOXYGEN=OFF \
        -DFFI_INCLUDE_DIR=$(pkg-config --cflags-only-I libffi | cut -c3-) \
        "$srcdir/llvm"

    make -C tools/clang
    make -C tools/cling
}

package() {
    cd "$srcdir/build"

    make DESTDIR="$pkgdir" install

    install -d "$pkgdir/usr/bin"
    ln -s "/opt/cling/bin/cling" "$pkgdir/usr/bin/cling"

    install -Dm644 "$srcdir/llvm/tools/cling/LICENSE.TXT" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

    # omit man page for clang's scan-build
    rm -f "$pkgdir/opt/cling/share/man/man1/scan-build.1"

    # remove empty directories
    rmdir -p --ignore-fail-on-non-empty "$pkgdir/opt/cling/share/man/man1"
    rmdir -p --ignore-fail-on-non-empty "$pkgdir/opt/cling/include/cling/cint"
}
