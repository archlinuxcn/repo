# Maintainer: Llewelyn Trahaearn <woefulderelict [at] gmail [dot] com>
# Contributor: Daniel Micay <danielmicay [at] gmail [dot] com>
# Contributor: MThinkCpp <mtc [dot] maintainer [at] outlook [dot] com>

pkgbase=libc++
pkgname=(${pkgbase}{,abi,experimental})
pkgver=6.0.0
pkgrel=1
url="https://libcxx.llvm.org/"
license=('MIT' 'custom:University of Illinois/NCSA Open Source License')
arch=('i686' 'x86_64')
depends=('gcc-libs')
makedepends=('clang' 'cmake' 'ninja' 'python' 'libunwind')
source=("https://releases.llvm.org/$pkgver/llvm-$pkgver.src.tar.xz"{,.sig}
        "https://releases.llvm.org/$pkgver/libcxx-$pkgver.src.tar.xz"{,.sig}
        "https://releases.llvm.org/$pkgver/libcxxabi-$pkgver.src.tar.xz"{,.sig})
noextract=("${source[@]##*/}")
sha512sums=('a71fdd5ddc46f01327ad891cfcc198febdbe10769c57f14d8a4fb7d514621ee4080e1a641200d3353c16a16731d390270499ec6cd3dc98fadc570f3eb6b52b8c'
            'SKIP'
            '3d93910f85a778f36c5f7a4429639008acba5713a2c8ac79a9de09463af6f9a388af45d39af23423a7223660701697ba067f3391f25d5a970973691dd88635e3'
            'SKIP'
            'c5e4cc05105770b42b20595fdbda5e1483be4582bc94335da1a15531ba43a0ecf30e1e0a252f62d4d0e6c79cda9d44ff5fdbe69a0a295b2431fd6de158410e2e'
            'SKIP')
validpgpkeys=(# Tom Stellard <tom@stellard.net> (.1 releases)
              # https://pgp.mit.edu/pks/lookup?op=get&search=0x8F0871F202119294
              11E521D646982372EB577A1F8F0871F202119294
              # Hans Wennborg <hans@chromium.org> (.0 releases)
              # https://releases.llvm.org/6.0.0/hans-gpg-key.asc
              B6C8F98282B944E3B0D5C2530FC3042E345AD05D)
 
prepare() {
  [[ -d llvm ]] || mkdir llvm
  bsdtar --strip-components 1 --uid 0 --gid 0 -zxf \
         ${srcdir}/${source[0]##*/} -C \
         llvm
  [[ -d llvm/projects/libcxx ]] || mkdir llvm/projects/libcxx
  bsdtar --strip-components 1 --uid 0 --gid 0 -zxf \
         ${srcdir}/${source[2]##*/} -C \
         llvm/projects/libcxx
  [[ -d llvm/projects/libcxxabi ]] || mkdir  llvm/projects/libcxxabi
  bsdtar --strip-components 1 --uid 0 --gid 0 -zxf \
         ${srcdir}/${source[4]##*/} -C \
         llvm/projects/libcxxabi
  sed -i 's/CREDITS.TXT/CREDITS/' llvm/projects/libcxx/LICENSE.TXT
  sed -i 's/CREDITS.TXT/CREDITS/' llvm/projects/libcxxabi/LICENSE.TXT
  [[ -d build ]] || mkdir build
}
 
build() {
  cd build
  cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DLIBCXX_ENABLE_EXPERIMENTAL_LIBRARY=On \
    -DLIBCXX_INSTALL_EXPERIMENTAL_LIBRARY=Off \
    ${srcdir}/llvm
  ninja cxx cxx_experimental
}

check() {
  cd build
  ninja check-cxx
}

package_libc++() {
  pkgdesc='LLVM C++ standard library.'
  depends=("libc++abi=${pkgver}-${pkgrel}")
  cd ${srcdir}/build
  DESTDIR="${pkgdir}" ninja install-libcxx

  # Remove ABI headers.
  rm "${pkgdir}/usr/include/c++/v1/cxxabi.h"
  rm "${pkgdir}/usr/include/c++/v1/__cxxabi_config.h"

  # Remove experimental headers.
  rm -rf "${pkgdir}/usr/include/c++/v1/experimental"

  # License.
  install -Dm644 ${srcdir}/llvm/projects/libcxx/CREDITS.TXT "${pkgdir}/usr/share/licenses/${pkgname}/CREDITS"
  install -Dm644 ${srcdir}/llvm/projects/libcxx/LICENSE.TXT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
 
package_libc++abi() {
  pkgdesc='Low level support for the LLVM C++ standard library.'
  cd ${srcdir}/build
  DESTDIR="${pkgdir}" ninja install-libcxxabi
  install -Dm644 ${srcdir}/build/include/c++/v1/cxxabi.h "${pkgdir}/usr/include/c++/v1/cxxabi.h"
  install -Dm644 ${srcdir}/build/include/c++/v1/__cxxabi_config.h "${pkgdir}/usr/include/c++/v1/__cxxabi_config.h"
  install -Dm644 ${srcdir}/llvm/projects/libcxxabi/CREDITS.TXT "${pkgdir}/usr/share/licenses/${pkgname}/CREDITS"
  install -Dm644 ${srcdir}/llvm/projects/libcxxabi/LICENSE.TXT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
 
package_libc++experimental() {
  depends=("libc++=$pkgver-$pkgrel")
  pkgdesc='LLVM C++ experimental library.'
  install -Dm644 ${srcdir}/build/lib/libc++experimental.a ${pkgdir}/usr/lib/libc++experimental.a
  install -d ${pkgdir}/usr/include/c++/v1/experimental
  install -m644 ${srcdir}/build/include/c++/v1/experimental/* ${pkgdir}/usr/include/c++/v1/experimental
  install -Dm644 ${srcdir}/llvm/projects/libcxx/CREDITS.TXT "${pkgdir}/usr/share/licenses/${pkgname}/CREDITS"
  install -Dm644 ${srcdir}/llvm/projects/libcxx/LICENSE.TXT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
