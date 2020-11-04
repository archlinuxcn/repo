# Maintainer: GordonGR <ntheo1979@gmail.com>
# Contributor: Gaetan Bisson <bisson@archlinux.org> 
# Contributor: said <atvordhosbn[at]gmail[dot]com>

pkgname=lib32-libcue
_pkgname=libcue
pkgver=2.2.1
pkgrel=1
pkgdesc='Parses so-called cue sheets and handles the parsed data (lib32)'
url='http://github.com/lipnitsk/libcue/'
arch=('x86_64')
license=('GPL2')
source=("${_pkgname}-$pkgver.tar.gz::https://github.com/lipnitsk/libcue/archive/v$pkgver.tar.gz")
depends=('lib32-glibc' 'libcue')
makedepends=('cmake')
md5sums=('1dfe65751c3817c76a107bd5a0d924a3')

build() {
cd ${_pkgname}-${pkgver}

export CC="gcc -m32"
export CXX="g++ -m32"
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

cmake -DCMAKE_INSTALL_PREFIX=/usr \
  -DCMAKE_INSTALL_LIBDIR=/usr/lib32 \
   -DBUILD_SHARED_LIBS=ON . \
  -DCC="gcc -m32" \
  -DCXX="g++ -m32" \
  -DPKG_CONFIG_PATH="/usr/lib32/pkgconfig"

make
}

package() {
cd ${_pkgname}-${pkgver}
make DESTDIR="${pkgdir}" install

cd "$pkgdir/usr"
rm -rf {bin,include,share/imlib2}/
#mv lib/ lib32/

cd "${pkgdir}/usr/lib32/pkgconfig"
sed -i 's|includedir=${prefix}/include|includedir=${prefix}/include/libcue/|' libcue.pc
sed -i 's|libdir=${prefix}/lib|libdir=${prefix}/lib32|' libcue.pc
}
