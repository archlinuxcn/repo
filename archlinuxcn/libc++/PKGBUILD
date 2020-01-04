# Maintainer: Llewelyn Trahaearn <woefulderelict [at] gmail [dot] com>
# Contributor: Daniel Micay <danielmicay [at] gmail [dot] com>
# Contributor: MThinkCpp <mtc [dot] maintainer [at] outlook [dot] com>

pkgbase=libc++
pkgname=(${pkgbase}{,abi,experimental})
pkgver=9.0.1
pkgrel=1
url="https://libcxx.llvm.org/"
license=('custom:Apache 2.0 with LLVM Exception')
arch=('i686' 'x86_64')
depends=('gcc-libs')
makedepends=('clang' 'cmake' 'llvm' 'libunwind' 'ninja' 'python')
source=("https://github.com/llvm/llvm-project/releases/download/llvmorg-$pkgver/llvm-$pkgver.src.tar.xz"{,.sig}
        "https://github.com/llvm/llvm-project/releases/download/llvmorg-$pkgver/libcxx-$pkgver.src.tar.xz"{,.sig}
        "https://github.com/llvm/llvm-project/releases/download/llvmorg-$pkgver/libcxxabi-$pkgver.src.tar.xz")
noextract=("${source[@]##*/}")
sha512sums=('bfb6960a4dd1e18f4005f324f478a781c69e8ec7c20569d9b243fcb9372dc7733b254f26c683373537990cc9c109c78eaf0f65449629ee17caca1bce9b9ccccd'
            'SKIP'
            'aabbc98c5bd6935d3dabfb309dfc171fbc16441396628d22d8dcdb89a5015f8fdedef4237134b841314d572205f7d5cfe44c1c8900db0f0156810f7810376bb2'
            'SKIP'
            'b5dbe4379a13046e7b9003e6913b0435271476feef0acbfd4e8207fca6d4a580182628866bd2032ce84a55d524fee8620841f17214bc79c8f46a3fde2f57627a')
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

# Deprecated function finally removed in Python 3.8 results in failure.
# https://github.com/llvm/llvm-project/issues/62
#check() {
#  cd build
#  ninja check-cxx check-cxxabi
#}

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
