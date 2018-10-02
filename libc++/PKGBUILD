# Maintainer: Llewelyn Trahaearn <woefulderelict [at] gmail [dot] com>
# Contributor: Daniel Micay <danielmicay [at] gmail [dot] com>
# Contributor: MThinkCpp <mtc [dot] maintainer [at] outlook [dot] com>

pkgbase=libc++
pkgname=(${pkgbase}{,abi,experimental})
pkgver=7.0.0
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
sha512sums=('bdc9b851c158b17e1bbeb7ac5ae49821bfb1251a3826fe8a3932cd1a43f9fb0d620c3de67150c1d9297bf0b86fa917e75978da29c3f751b277866dc90395abec'
            'SKIP'
            '5ebf8418bc9d311c1744c257ab7a26cf2436a64a47451905df70ec64b12d25ec33acf99e1b9d552fd54ed850bed8f53dffde2ea20292ecd9976eaa31f144caf5'
            'SKIP'
            '95aa8f60477739e6d6eb6ba1e32c98928e1b8104d18d659336cf7f1c5bfd1ed505015077dfbe39329c0c9d2b5b428d853e5652b0106c0cde317d2d013ebd1cf0'
            'SKIP')
# see https://releases.llvm.org/download.html
validpgpkeys=(# Tom Stellard <tstellar@redhat.com> (.1 releases)
              # https://pgp.mit.edu/pks/lookup?op=get&search=0xA2C794A986419D8A
              474E22316ABF4785A88C6E8EA2C794A986419D8A
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
  install -Dm644 -t ${pkgdir}/usr/include/c++/v1/experimental ${srcdir}/build/include/c++/v1/experimental/*
  install -Dm644 ${srcdir}/llvm/projects/libcxx/CREDITS.TXT "${pkgdir}/usr/share/licenses/${pkgname}/CREDITS"
  install -Dm644 ${srcdir}/llvm/projects/libcxx/LICENSE.TXT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
