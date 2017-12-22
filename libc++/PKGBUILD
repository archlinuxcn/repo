# Maintainer: Llewelyn Trahaearn <woefulderelict [at] gmail [dot] com>
# Contributor: Daniel Micay <danielmicay [at] gmail [dot] com>
# Contributor: MThinkCpp <mtc [dot] maintainer [at] outlook [dot] com>

pkgbase=libc++
pkgname=(${pkgbase}{,abi,experimental})
pkgver=5.0.1
pkgrel=1
url="http://libcxx.llvm.org/"
license=('MIT' 'custom:University of Illinois/NCSA Open Source License')
arch=('i686' 'x86_64')
depends=('gcc-libs')
makedepends=('clang' 'cmake' 'python' 'libunwind')
source=("https://releases.llvm.org/$pkgver/llvm-$pkgver.src.tar.xz"{,.sig}
        "https://releases.llvm.org/$pkgver/libcxx-$pkgver.src.tar.xz"{,.sig}
        "https://releases.llvm.org/$pkgver/libcxxabi-$pkgver.src.tar.xz"{,.sig})
noextract=("${source[@]##*/}")
sha512sums=('bee1d45fca15ce725b1f2b1339b13eb6f750a3a321cfd099075477ec25835a8ca55b5366172c4aad46592dfd8afe372349ecf264f581463d017f9cee2d63c1cb'
            'SKIP'
            '994681d3c79047fc2d618c5584b08e9b5c925dab48f8812fc0adc81a575b49a637e9481bb9a0f7ae6f7f352b2b33f40056c347c27123cd6c96c6c226febd002c'
            'SKIP'
            'a8d448653772690a19f68c1270f9cf18f27d7225847825f29c6ea21846c1074aa61c31b81bc2ae4007067985d389071c32e69b2560282ddb85864a99e9bdd884'
            'SKIP')
validpgpkeys=(# Tom Stellard <tom@stellard.net> (.1 releases)
              # https://pgp.mit.edu/pks/lookup?op=get&search=0x8F0871F202119294
              11E521D646982372EB577A1F8F0871F202119294
              # Hans Wennborg <hans@chromium.org> (.0 releases)
              # http://releases.llvm.org/4.0.0/hans-gpg-key.asc
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
