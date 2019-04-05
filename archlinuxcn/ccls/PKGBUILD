# Maintainer: Fangrui Song <i at maskray.me>

pkgname=ccls
pkgver=0.20190314
pkgrel=1
pkgdesc='C/C++/ObjC language server supporting cross references, hierarchies, completion and semantic highlighting'
arch=('x86_64')
url='https://github.com/MaskRay/ccls'
license=('Apache')
depends=('clang' 'llvm-libs' 'rapidjson')
makedepends=("cmake" "git" "llvm")
conflicts=('ccls-git')
source=("https://github.com/MaskRay/$pkgname/archive/$pkgver.tar.gz")
sha256sums=('SKIP')

prepare() {
  cd $pkgname-$pkgver
}

build() {
  cd $pkgname-$pkgver
  cmake -H. -Bbuild -DCMAKE_INSTALL_PREFIX=/usr
  cmake --build build
}

package() {
  cd $pkgname-$pkgver/build
  make DESTDIR="$pkgdir" install
}
