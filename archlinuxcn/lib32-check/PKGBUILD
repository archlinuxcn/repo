# Maintainer: Andrew Sun <adsun701@gmail.com>
# Contributor: orumin <dev@orum.in>

_basename=check
pkgname="lib32-$_basename"
pkgver=0.12.0
pkgrel=1
pkgdesc="A unit testing framework for C (32-bit)"
arch=('x86_64')
url="https://libcheck.github.io/check/"
license=('LGPL')
depends=('lib32-glibc' 'awk' "$_basename")
makedepends=('git' 'lib32-gcc-libs')
_commit=673dce1d61781c32b449bef0ee8711dc7e689170  # tags/0.12.0
source=("git+https://github.com/libcheck/check#commit=$_commit")
md5sums=('SKIP')

pkgver() {
  cd $_basename
  git describe --tags | sed 's/-/+/g'
}

prepare() {
  cd $_basename
  autoreconf -fvi
}

build() {
  cd $_basename

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure --prefix=/usr --disable-static \
    --libdir=/usr/lib32 
  make
}

check() {
  cd $_basename
  # Extremely long
  #make -k check
}

package() {
  cd $_basename
  make DESTDIR="$pkgdir" install
  rm -rf ${pkgdir}/usr/{bin,share,include}

}
