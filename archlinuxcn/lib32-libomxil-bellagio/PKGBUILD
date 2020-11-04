# Maintainer: Alexandre Demers <alexandre.f.demers@gmail.com>

_pkgbase=libomxil-bellagio
pkgname=lib32-$_pkgbase
pkgver=0.9.3
pkgrel=6
pkgdesc="An opensource implementation of the OpenMAX Integration Layer API"
arch=('x86_64')
url="http://omxil.sourceforge.net"
license=('LGPL')
depends=("lib32-glibc" "$_pkgbase")
makedepends=("lib32-gcc-libs")
source=("https://downloads.sourceforge.net/project/omxil/omxil/Bellagio%200.9.3/${_pkgbase}-${pkgver}.tar.gz"
        fedora-fixes.patch)
md5sums=('a1de827fdb75c02c84e55f740ca27cb8'
         'c34f9facf0cf26171c81f2fc3d562ec6')

prepare() {
  cd ${srcdir}/${_pkgbase}-$pkgver

  # Fixes from fedora repo
  patch -Np1 -i ../fedora-fixes.patch
  sed -e 's/-Werror//' -i configure.ac
  autoreconf -fiv
}

build() {
  cd ${srcdir}/${_pkgbase}-${pkgver}

  export CC="gcc -m32"
  CFLAGS+=' -fcommon' # https://wiki.gentoo.org/wiki/Gcc_10_porting_notes/fno_common
  
  ./configure --prefix=/usr --disable-static --libdir=/usr/lib32

  make
}

package() {
  cd ${srcdir}/${_pkgbase}-${pkgver}
  make DESTDIR="${pkgdir}" install

  rm -rf "$pkgdir"/usr/{bin,include,share}
}
