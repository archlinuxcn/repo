# Maintainer: Llewelyn Trahaearn <woefulderelict [at] gmail [dot] com>
# Contributor: Daniel Micay <danielmicay [at] gmail [dot] com>
# Contributor: MThinkCpp <mtc [dot] maintainer [at] outlook [dot] com>

pkgbase=libc++
pkgname=(${pkgbase}{,abi,experimental})
pkgver=8.0.0
pkgrel=2
url="https://libcxx.llvm.org/"
license=('MIT' 'custom:University of Illinois/NCSA Open Source License')
arch=('i686' 'x86_64')
depends=('gcc-libs')
makedepends=('clang' 'cmake' 'ninja' 'python' 'libunwind')
source=("https://releases.llvm.org/$pkgver/llvm-$pkgver.src.tar.xz"{,.sig}
        "https://releases.llvm.org/$pkgver/libcxx-$pkgver.src.tar.xz"{,.sig}
        "https://releases.llvm.org/$pkgver/libcxxabi-$pkgver.src.tar.xz"{,.sig})
noextract=("${source[@]##*/}")
sha512sums=('1602343b451b964f5d8c2d6b0654d89384c80d45883498c5f0e2f4196168dd4a1ed2a4dadb752076020243df42ffe46cb31d82ffc145d8e5874163cbb9686a1f'
            'SKIP'
            '2e0fcd3e78f7e15ea894e52c51351daef8e3a2aaf53b3df7497b11403d28f5269ff49a4674bacea1d565a5faa2b24502caaaeff9cd48518f0d141563d8f9cc03'
            'SKIP'
            '9ee2e6d5899529be45b2e5edc395606fa9040d25789b3da1ae0182113626e7624cbb071eae525c478293a7b371876e41614348ee5808f90f3f9c7b08837e1055'
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
    -DLIBCXX_INSTALL_FILESYSTEM_LIBRARY=NO \
    "$srcdir"/llvm
  ninja cxx cxx_experimental cxx_filesystem
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
  
  install -Dm0644 -t "$pkgdir"/usr/lib/ build/lib/libc++experimental.a build/lib/libc++fs.a
  install -Dm0644 llvm/projects/libcxx/CREDITS.TXT "$pkgdir"/usr/share/licenses/"$pkgname"/CREDITS
  install -Dm0644 llvm/projects/libcxx/LICENSE.TXT "$pkgdir"/usr/share/licenses/"$pkgname"/LICENSE
}
