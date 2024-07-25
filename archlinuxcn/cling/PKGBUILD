# Maintainer: archibald869 <archibald869 at web dot de>

pkgname=cling
pkgver=1.0
pkgrel=1
pkgdesc="Interactive C++ interpreter, built on the top of LLVM and Clang libraries"
arch=("i686" "x86_64")
url="https://root.cern/cling/"
license=("custom:Cling Release License")
provides=("cling")
conflicts=("cling")
depends=("libxml2")
makedepends=("git" "cmake" "ninja" "python")
optdepends=(
    "perl: support for scan-build, ccc-analyzer and c++-analyzer"
    "python: support for scan-view and Jupyter"
    "python-pygments: support for opt-viewer"
    "python-yaml: support for opt-viewer"
)
source=(
    "cling-llvm::git+https://github.com/root-project/llvm-project.git#tag=cling-llvm13-20240318-01"
    "cling::git+https://github.com/root-project/cling.git#tag=v$pkgver"
)
sha256sums=(
    "SKIP"
    "SKIP"
)
options=(!lto !debug)


build() {
    mkdir -p "$srcdir/build"
    cd "$srcdir/build"

    cmake \
        -G Ninja \
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
        -DLLVM_EXTERNAL_PROJECTS=cling \
        -DLLVM_EXTERNAL_CLING_SOURCE_DIR="$srcdir/cling" \
        -DLLVM_ENABLE_PROJECTS=clang \
        "$srcdir/cling-llvm/llvm"

    ninja
}

package() {
    cd "$srcdir/build"

    DESTDIR="$pkgdir" ninja install

    install -d "$pkgdir/usr/bin"
    ln -s "/opt/cling/bin/cling" "$pkgdir/usr/bin/cling"

    install -Dm644 "$srcdir/cling/LICENSE.TXT" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

    # include CMake target import file so that other packages are able to use
    # `find_package(Cling REQUIRED)`
    install -Dm644 "$srcdir/build/tools/cling/lib/cmake/cling/ClingTargets.cmake" \
        "$pkgdir/opt/cling/lib/cmake/cling"

    # adjust cling target locations
    sed -Ei 's#(IMPORTED_LOCATION_RELEASE) ".*/([^/]*)"#\1 "/opt/cling/lib/\2"#g' \
        "$pkgdir/opt/cling/lib/cmake/cling/ClingTargets.cmake"

    # omit man page for clang's scan-build
    rm -f "$pkgdir/opt/cling/share/man/man1/scan-build.1"

    # remove empty directories
    rmdir -p --ignore-fail-on-non-empty "$pkgdir/opt/cling/share/man/man1"
    rmdir -p --ignore-fail-on-non-empty "$pkgdir/opt/cling/include/cling/cint"
}
