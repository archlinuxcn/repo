# Maintainer: Llewelyn Trahaearn <woefulderelict [at] gmail [dot] com>
# Contributor: Daniel Micay <danielmicay [at] gmail [dot] com>
# Contributor: MThinkCpp <mtc [dot] maintainer [at] outlook [dot] com>

pkgbase=libc++
pkgname=(${pkgbase}{,abi,experimental})
pkgver=9.0.0
pkgrel=1
url="https://libcxx.llvm.org/"
license=('custom:Apache 2.0 with LLVM Exception')
arch=('i686' 'x86_64')
depends=('gcc-libs')
makedepends=('clang' 'cmake' 'llvm' 'libunwind' 'ninja' 'python')
source=("https://releases.llvm.org/$pkgver/llvm-$pkgver.src.tar.xz"{,.sig}
        "https://releases.llvm.org/$pkgver/libcxx-$pkgver.src.tar.xz"{,.sig}
        "https://releases.llvm.org/$pkgver/libcxxabi-$pkgver.src.tar.xz"{,.sig})
noextract=("${source[@]##*/}")
sha512sums=('1bb3341e1d231559b948f1505b33c2e2e03989f9b8bbfef0e0cdaff5ac43f85574c9ec5ac53399b914f497d6899425d861411024e8d7e1d1a338c1c6951ac658'
            'SKIP'
            'cbaca724c4f3e3a270dfd53aac50cbb920190fe55486b164d52e73845819dd22afb10c23f5875da59d433fd5b96a0f153208746117309ac1267a38fa56f4818e'
            'SKIP'
            '261f32f61814728ce61c830c80192a55e1ba03c50f49712e208052444ac3acc6d7efcbd7b76a505292f9233aad23b00180aca4e72326ae1244385b39f226e625'
            'SKIP')
validpgpkeys=('474E22316ABF4785A88C6E8EA2C794A986419D8A') # Tom Stellard <tstellar@redhat.com> (.1 releases)
validpgpkeys+=('B6C8F98282B944E3B0D5C2530FC3042E345AD05D') # Hans Wennborg <hans@chromium.org> (.0 releases)
 
prepare() {
  mkdir -p build llvm/projects/libcxx llvm/projects/libcxxabi
  bsdtar --strip-components 1 -zxf "${source[0]##*/}" -C llvm
  bsdtar --strip-components 1 -zxf "${source[2]##*/}" -C llvm/projects/libcxx
  bsdtar --strip-components 1 -zxf "${source[4]##*/}" -C llvm/projects/libcxxabi
  sed -i 's/CREDITS.TXT/CREDITS/' llvm/projects/libcxx/LICENSE.TXT llvm/projects/libcxxabi/LICENSE.TXT
}
 
build() {
  cd build
  cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DLIBCXX_INSTALL_EXPERIMENTAL_LIBRARY=NO \
    "$srcdir"/llvm
  ninja cxx cxx_experimental
}

check() {
  cd build
  ninja check-cxx check-cxxabi
}

package_libc++() {
  pkgdesc='LLVM C++ standard library.'
  depends=("libc++abi=$pkgver-$pkgrel")
  options=('staticlibs')

  cd build
  DESTDIR="$pkgdir" ninja install-libcxx

  # License.
  install -Dm0644 "$srcdir"/llvm/projects/libcxx/CREDITS.TXT "$pkgdir"/usr/share/licenses/"$pkgname"/CREDITS
  install -Dm0644 "$srcdir"/llvm/projects/libcxx/LICENSE.TXT "$pkgdir"/usr/share/licenses/"$pkgname"/LICENSE
}
 
package_libc++abi() {
  pkgdesc='Low level support for the LLVM C++ standard library.'
  options=('staticlibs')
  
  cd build
  DESTDIR="$pkgdir" ninja install-libcxxabi
  install -Dm0644 "$srcdir"/llvm/projects/libcxxabi/CREDITS.TXT "$pkgdir"/usr/share/licenses/"$pkgname"/CREDITS
  install -Dm0644 "$srcdir"/llvm/projects/libcxxabi/LICENSE.TXT "$pkgdir"/usr/share/licenses/"$pkgname"/LICENSE
}
 
package_libc++experimental() {
  depends=("libc++=$pkgver-$pkgrel")
  pkgdesc='LLVM C++ experimental library.'
  
  install -Dm0644 -t "$pkgdir"/usr/lib/ build/lib/libc++experimental.a
  install -Dm0644 llvm/projects/libcxx/CREDITS.TXT "$pkgdir"/usr/share/licenses/"$pkgname"/CREDITS
  install -Dm0644 llvm/projects/libcxx/LICENSE.TXT "$pkgdir"/usr/share/licenses/"$pkgname"/LICENSE
}
