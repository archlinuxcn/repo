# Maintainer: Fangrui Song <i at maskray.me>

pkgname=ccls
pkgver=0.20190823.4
pkgrel=3
pkgdesc='C/C++/ObjC language server supporting cross references, hierarchies, completion and semantic highlighting'
arch=('x86_64')
url='https://github.com/MaskRay/ccls'
license=('Apache')
depends=('clang' 'llvm-libs' 'rapidjson')
makedepends=("cmake" "git" "llvm")
conflicts=('ccls-git')
source=("https://github.com/MaskRay/$pkgname/archive/$pkgver.tar.gz")
sha256sums=('19f394b69d70415d3be9a11a030e0bb28ddc2b654cbfa35f4570096935f9f536')

prepare() {
  cd $pkgname-$pkgver
}

build() {
  cd $pkgname-$pkgver
  cmake -H. -Bbuild -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_CXX_COMPILER=clang++
  cmake --build build
}

package() {
  cd $pkgname-$pkgver/build
  make DESTDIR="$pkgdir" install
}
