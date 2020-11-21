# Maintainer: Llewelyn Trahaearn <woefulderelict [at] gmail [dot] com>
# Contributor: Daniel Micay <danielmicay [at] gmail [dot] com>
# Contributor: MThinkCpp <mtc [dot] maintainer [at] outlook [dot] com>

pkgbase=libc++
pkgname=(${pkgbase}{,abi,experimental})
pkgver=11.0.0
pkgrel=1
url="https://libcxx.llvm.org/"
license=('custom:Apache 2.0 with LLVM Exception')
arch=('i686' 'x86_64')
depends=('gcc-libs')
makedepends=('clang' 'cmake' 'llvm' 'libunwind' 'ninja' 'python')
source=("https://github.com/llvm/llvm-project/releases/download/llvmorg-$pkgver/llvm-$pkgver.src.tar.xz"{,.sig}
        "https://github.com/llvm/llvm-project/releases/download/llvmorg-$pkgver/libcxx-$pkgver.src.tar.xz"{,.sig}
        "https://github.com/llvm/llvm-project/releases/download/llvmorg-$pkgver/libcxxabi-$pkgver.src.tar.xz"{,.sig})
noextract=("${source[@]##*/}")
sha512sums=('b3e92091ac48772edc0c30801218ce646ef374e1968baab91df9005f58e11c3ce149b2c4c655c7001f8554fd337caa02c08783bc736153bf58f35fe008e624a4'
            'SKIP'
            'c4360c330c27caa940b6881775e37f4801152ef9f12fe5ba754aa5d38214e588e975d760a79866d1eb26f9fba9ce9082c4248f0ac2e7d635d976b9456cc1a4aa'
            'SKIP'
            'bfefe9784c9b466844d46e9882b93409b226277b3d98f05ff096a9b533fe1b112687122179e6e8678670f950968dbae7accf3f6ab0f0784cfb316ccab981dbcf'
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
  # https://wiki.archlinux.org/index.php/Clang#Build_packages_with_Clang
  CFLAGS=${CFLAGS/-fvar-tracking-assignments}
  CXXFLAGS=${CXXFLAGS/-fvar-tracking-assignments}

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
  DESTDIR="$pkgdir" ninja install-cxx

  # License.
  install -Dm0644 "$srcdir"/llvm/projects/libcxx/CREDITS.TXT "$pkgdir"/usr/share/licenses/"$pkgname"/CREDITS
  install -Dm0644 "$srcdir"/llvm/projects/libcxx/LICENSE.TXT "$pkgdir"/usr/share/licenses/"$pkgname"/LICENSE
}
 
package_libc++abi() {
  pkgdesc='Low level support for the LLVM C++ standard library.'
  options=('staticlibs')
  
  cd build
  DESTDIR="$pkgdir" ninja install-cxxabi
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
