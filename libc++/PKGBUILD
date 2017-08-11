# Maintainer: Llewelyn Trahaearn <woefulderelict [at] gmail [dot] com>
# Contributor: Daniel Micay <danielmicay [at] gmail [dot] com>
# Contributor: MThinkCpp <mtc [dot] maintainer [at] outlook [dot] com>

pkgbase=libc++
pkgname=(${pkgbase}{,abi,experimental})
pkgver=4.0.1
pkgrel=1
url="http://libcxx.llvm.org/"
license=('MIT' 'custom:University of Illinois/NCSA Open Source License')
arch=('i686' 'x86_64')
depends=('gcc-libs')
makedepends=('clang' 'cmake' 'python' 'libunwind')
source=("http://llvm.org/releases/$pkgver/llvm-$pkgver.src.tar.xz"{,.sig}
        "http://llvm.org/releases/$pkgver/libcxx-$pkgver.src.tar.xz"{,.sig}
        "http://llvm.org/releases/$pkgver/libcxxabi-$pkgver.src.tar.xz"{,.sig})
noextract=("${source[@]##*/}")
sha512sums=('16adc39b34ddb628f81b171119a8e2a0e9138b25011e803ef0b688e2fbea116fc4953d3a1b61b90a98a75e33619f81566b7cb06a9a2ea4d04ac5e0eb303a2d1d'
            'SKIP'
            '91f3f397be606989be99865d0b279557f9afb93f7a74ed10c3a74f4440e38b5694ddf452bbf2f487cacd4391606dd5c7edfe5130f2de19e2acfd6cce619d028a'
            'SKIP'
            'e94315ba8a507d8481d70c33e7ab2d724d51726edb8412c70a1b5f59e3f15d5825f1502dc2db138b20e5293fb90a184050be94d5ac270fd7ce78b502efb9f86a'
            'SKIP')
validpgpkeys=(# Tom Stellard <tom@stellard.net> (.1 releases)
              # https://pgp.mit.edu/pks/lookup?op=get&search=0x8F0871F202119294
              11E521D646982372EB577A1F8F0871F202119294
              # Hans Wennborg <hans@chromium.org> (.0 releases)
              # http://releases.llvm.org/3.8.0/hans-gpg-key.asc
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
  CC=clang CXX=clang++ cmake \
    -G "Unix Makefiles" \
    -DLIBCXX_ENABLE_EXPERIMENTAL_LIBRARY=On \
    -DLIBCXX_INSTALL_EXPERIMENTAL_LIBRARY=Off \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    ${srcdir}/llvm
  make cxx cxx_experimental
}

package_libc++() {
  pkgdesc='A new implementation of the C++ standard library, targeting C++11.'
  depends=("libc++abi=${pkgver}-${pkgrel}")
  cd ${srcdir}/build
  make DESTDIR="${pkgdir}" install-libcxx
  install -Dm644 ${srcdir}/llvm/projects/libcxx/CREDITS.TXT "${pkgdir}/usr/share/licenses/${pkgname}/CREDITS"
  install -Dm644 ${srcdir}/llvm/projects/libcxx/LICENSE.TXT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
 
package_libc++abi() {
  pkgdesc='A new implementation of low level support for a standard C++ library'
  cd ${srcdir}/build
  make DESTDIR="${pkgdir}" install-libcxxabi
  install -Dm644 ${srcdir}/build/include/c++/v1/cxxabi.h "${pkgdir}/usr/include/c++/v1/cxxabi.h"
  install -Dm644 ${srcdir}/build/include/c++/v1/__cxxabi_config.h "${pkgdir}/usr/include/c++/v1/__cxxabi_config.h"
  install -Dm644 ${srcdir}/llvm/projects/libcxxabi/CREDITS.TXT "${pkgdir}/usr/share/licenses/${pkgname}/CREDITS"
  install -Dm644 ${srcdir}/llvm/projects/libcxxabi/LICENSE.TXT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
 
package_libc++experimental() {
  depends=("libc++=$pkgver-$pkgrel")
  pkgdesc='A new implementation of the C++ standard library, targeting C++11 (experimental library)'
  install -Dm644 ${srcdir}/build/lib/libc++experimental.a ${pkgdir}/usr/lib/libc++experimental.a
  install -Dm644 ${srcdir}/llvm/projects/libcxx/CREDITS.TXT "${pkgdir}/usr/share/licenses/${pkgname}/CREDITS"
  install -Dm644 ${srcdir}/llvm/projects/libcxx/LICENSE.TXT "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
