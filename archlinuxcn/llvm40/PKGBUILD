# Maintainer: Maxime Arthaud <maxime@arthaud.me>
# Contributor: Evangelos Foutras <evangelos@foutrelis.com>
# Contributor: Jan "heftig" Steffens <jan.steffens@gmail.com>
# Contributor: Sebastian Nowicki <sebnow@gmail.com>
# Contributor: Devin Cofer <ranguvar{AT]archlinux[DOT}us>
# Contributor: Tobias Kieslich <tobias@justdreams.de>
# Contributor: Geoffroy Carrier <geoffroy.carrier@aur.archlinux.org>
# Contributor: Tomas Lindquist Olsen <tomas@famolsen.dk>
# Contributor: Roberto Alsina <ralsina@kde.org>
# Contributor: Gerardo Exequiel Pozzi <vmlinuz386@yahoo.com.ar>

pkgname=('llvm40' 'llvm40-libs' 'clang40')
pkgver=4.0.1
pkgrel=7
_prefix="/usr/lib/llvm-4.0"
arch=('i686' 'x86_64')
url="http://llvm.org/"
license=('custom:University of Illinois/NCSA Open Source License')
makedepends=('cmake' 'libffi' 'python2' 'libedit')
options=('staticlibs')
source=(https://releases.llvm.org/$pkgver/llvm-$pkgver.src.tar.xz{,.sig}
        https://releases.llvm.org/$pkgver/cfe-$pkgver.src.tar.xz{,.sig}
        https://releases.llvm.org/$pkgver/compiler-rt-$pkgver.src.tar.xz{,.sig}
        0001-GCC-compatibility-Ignore-the-fno-plt-flag.patch
        0002-Enable-SSP-and-PIE-by-default.patch
        PR31870-Disable-llvm-symbolizer-test.patch
        D35246-Fix-sanitizer-build-against-latest-glibc.patch
        PR37486-Fix-lli-fails-to-build-with-gcc-8.patch
        PR37031-Fix-Mips-breakages.patch
        PR37032-Fix-ldd-x86_64-darwin13-build-fails.patch
        D32089-Avoid-undefined-behavior-in-unittest.patch
        D47281-Use-pre-computed-size-of-struct-ustat.patch)
sha256sums=('da783db1f82d516791179fe103c71706046561f7972b18f0049242dee6712b51'
            'SKIP'
            '61738a735852c23c3bdbe52d035488cdb2083013f384d67c1ba36fabebd8769b'
            'SKIP'
            'a3c87794334887b93b7a766c507244a7cdcce1d48b2e9249fc9a94f2c3beb440'
            'SKIP'
            'ed4a1c3c73b31421caa0ba50d14cabc16de676a88f045d06b207bbb3006963ac'
            '79f1a409700a83d983d7237a907aeddf342c28aa810b87b28ee27b8c5560644a'
            '6fff47ab5ede79d45fe64bb4903b7dfc27212a38e6cd5d01e60ebd24b7557359'
            '0afff7e5cf0f6df596517f63a9a9f085eab3b53f42a1eb14bbd83861c36c9fd7'
            '080e90dabbd386fb8c4771ab7537acff157b72bb0f2591609805cacf684cceed'
            '506bdbcb30c8bb4a8e3406f14ae972441835dceede61ece9e0117cb0f357e514'
            '6d5498068cf4f6141ee2c8abc1828cc3797e309e545a4e80fa544ac253fc619b'
            '25121be62f3213030deb7db1ddf2d200971f8111c9d72a59e45db3ddca322bb2'
            'aa42070d84d055311d39d8020d1606e116687ef2c6d515364e55d3e1d42db98d')
validpgpkeys=('11E521D646982372EB577A1F8F0871F202119294')

prepare() {
  cd "$srcdir/llvm-$pkgver.src"
  mkdir build

  mv "$srcdir/cfe-$pkgver.src" tools/clang
  mv "$srcdir/compiler-rt-$pkgver.src" projects/compiler-rt

  # Enable SSP and PIE by default
  patch -Np1 -d tools/clang < ../0001-GCC-compatibility-Ignore-the-fno-plt-flag.patch
  patch -Np1 -d tools/clang < ../0002-Enable-SSP-and-PIE-by-default.patch

  # Disable test that fails when compiled as PIE
  # https://bugs.llvm.org/show_bug.cgi?id=31870
  patch -Np1 < ../PR31870-Disable-llvm-symbolizer-test.patch

  # Fix sanitizer build against latest glibc
  # https://reviews.llvm.org/D35246
  # https://gcc.gnu.org/bugzilla/show_bug.cgi?id=81066
  patch -Np0 -d projects/compiler-rt < ../D35246-Fix-sanitizer-build-against-latest-glibc.patch

  # Fix lli fails to build with GCC 8
  # https://bugs.llvm.org/show_bug.cgi?id=37486
  # https://bugzilla.redhat.com/show_bug.cgi?id=1540620
  patch -Np1 < ../PR37486-Fix-lli-fails-to-build-with-gcc-8.patch

  # Fix Mips breakages
  # https://bugs.llvm.org/show_bug.cgi?id=37031
  patch -Np0 < ../PR37031-Fix-Mips-breakages.patch

  # Fix lld-x86_64-darwin13 build fails
  # https://bugs.llvm.org/show_bug.cgi?id=37032
  patch -Np0 < ../PR37032-Fix-ldd-x86_64-darwin13-build-fails.patch

  # Avoid undefined behavior in unittest by not making a named ArrayRef from a std::initializer_list
  # https://reviews.llvm.org/D32089
  patch -Np0 < ../D32089-Avoid-undefined-behavior-in-unittest.patch

  # Use pre-computed size of struct ustat for Linux
  # https://reviews.llvm.org/D47281
  patch -Np0 -d projects/compiler-rt < ../D47281-Use-pre-computed-size-of-struct-ustat.patch
}

build() {
  cd "$srcdir/llvm-$pkgver.src/build"

  cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX="${_prefix}" \
    -DLLVM_BUILD_LLVM_DYLIB=ON \
    -DLLVM_LINK_LLVM_DYLIB=ON \
    -DLLVM_INSTALL_UTILS=ON \
    -DLLVM_ENABLE_RTTI=ON \
    -DLLVM_ENABLE_FFI=ON \
    -DLLVM_BUILD_TESTS=ON \
    -DCLANG_INSTALL_SCANBUILD=OFF \
    -DCLANG_INSTALL_SCANVIEW=OFF \
    -DFFI_INCLUDE_DIR=$(pkg-config --variable=includedir libffi) \
    -DLLVM_BINUTILS_INCDIR=/usr/include \
    ..

  make

  # Disable automatic installation of components that go into subpackages
  sed -i '/clang\/cmake_install.cmake/d' tools/cmake_install.cmake
  sed -i '/extra\/cmake_install.cmake/d' tools/clang/tools/cmake_install.cmake
  sed -i '/compiler-rt\/cmake_install.cmake/d' projects/cmake_install.cmake
}

check() {
  cd "$srcdir/llvm-$pkgver.src/build"
  make check-{llvm,clang}
}

package_llvm40() {
  pkgdesc="Low Level Virtual Machine"
  depends=('llvm40-libs' 'perl')

  cd "$srcdir/llvm-$pkgver.src"

  make -C build DESTDIR="$pkgdir" install

  # The runtime libraries go into llvm-libs
  mv -f "${pkgdir}${_prefix}"/lib/lib{LLVM,LTO}*.so* "$srcdir"
  mv -f "${pkgdir}${_prefix}"/lib/LLVMgold.so "$srcdir"

  install -Dm644 LICENSE.TXT "${pkgdir}${_prefix}/share/licenses/llvm/LICENSE"

  # add symbolic links in /usr/bin
  mkdir -p "$pkgdir/usr/bin"
  cd "${pkgdir}${_prefix}"/bin
  for f in *; do
    ln -s "${_prefix}/bin/$f" "$pkgdir/usr/bin/${f%-4.0}-4.0"
  done
}

package_llvm40-libs() {
  pkgdesc="Low Level Virtual Machine (runtime libraries)"
  depends=('gcc-libs' 'zlib' 'libffi' 'libedit' 'ncurses')

  install -d "${pkgdir}${_prefix}/lib"
  cp -P \
    "$srcdir"/lib{LLVM,LTO}*.so* \
    "$srcdir"/LLVMgold.so \
    "${pkgdir}${_prefix}/lib/"

  install -Dm644 "$srcdir/llvm-$pkgver.src/LICENSE.TXT" \
    "${pkgdir}${_prefix}/share/licenses/llvm-libs/LICENSE"
}

package_clang40() {
  pkgdesc="C language family frontend for LLVM"
  url="http://clang.llvm.org/"
  depends=('llvm40-libs' 'gcc' 'libxml2')
  optdepends=('openmp: OpenMP support in clang with -fopenmp'
              'python2: for scan-view and git-clang-format')

  cd "$srcdir/llvm-$pkgver.src"

  make -C build/tools/clang DESTDIR="$pkgdir" install
  make -C build/projects/compiler-rt DESTDIR="$pkgdir" install

  install -Dm644 tools/clang/LICENSE.TXT \
    "${pkgdir}${_prefix}/share/licenses/clang/LICENSE"

  # add symbolic links in /usr/bin
  mkdir -p "$pkgdir/usr/bin"
  cd "${pkgdir}${_prefix}"/bin
  for f in *; do
    ln -f -s "${_prefix}/bin/$f" "$pkgdir/usr/bin/${f%-4.0}-4.0"
  done
}

# vim:set ts=2 sw=2 et:
