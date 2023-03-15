# Maintainer: tytan652 <tytan652 at tytanium dot xyz>

pkgname=libajantv2
_pkgver=16.2-bugfix5
pkgver=${_pkgver//-/_}
pkgrel=1
epoch=1
pkgdesc="AJA NTV2 Open Source Static Libs and Headers for building applications that only wish to statically link against"
arch=("i686" "x86_64" "aarch64")
url="https://github.com/aja-video/ntv2"
license=("MIT")
depends=()
makedepends=("cmake" "git")
options=('!lto' 'debug')
source=("ntv2::git+https://github.com/aja-video/ntv2.git#commit=0acbac70a0b5e6509cca78cfbf69974c73c10db9")
sha256sums=("SKIP")

build() {
  cd ntv2
  mkdir -p build; cd build

  cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DAJA_BUILD_OPENSOURCE=ON \
    -DAJA_BUILD_APPS=OFF \
    -DAJA_BUILD_SHARED=ON \
    -DAJA_INSTALL_HEADERS=ON ..

  make
}

package() {
  cd ntv2
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  
  cd build
  make install DESTDIR="$pkgdir"
}
