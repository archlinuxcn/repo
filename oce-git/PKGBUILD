# Maintainer: Yichao Yu <yyc1992@gmail.com>
# Contributor: Giuseppe Borzi <gborzi@ieee.org>
# Contributor: Brice M<E9>alier <mealier_brice@yahoo.fr>
# Contributor: Michele Mocciola <mickele>

pkgname=oce-git
pkgver=0.16.0.29.g6d4ba0e
pkgrel=1
pkgdesc="Open CASCADE community edition, 3D modeling & numerical simulation"
arch=('i686' 'x86_64')
url="http://www.opencascade.org"
license=('custom')
depends=(freeimage freetype2 mesa libgl glu 'libcl>=1.2' libx11 tk)
makedepends=(cmake git opencl-headers12)
optdepends=(java-runtime)
provides=("opencascade=6.7.1")
conflicts=("opencascade")
options=(!libtool debug)
source=(git://github.com/tpaviot/oce)
md5sums=('SKIP')

pkgver() {
  cd oce

  git describe | sed -e 's/^[^0-9]*//' -e 's/-/.0./' -e 's/-/./g'
}

build() {
  cd oce
  mkdir -p build
  cd build
  export CFLAGS+=' -DGLX_GLXEXT_LEGACY'
  export CXXFLAGS+=' -DGLX_GLXEXT_LEGACY'
  cmake .. -DOCE_INSTALL_PREFIX=/usr -DOCE_WITH_OPENCL=On \
        -DOCE_WITH_FREEIMAGE=On
  make
}

package() {
  cd oce/build

  make install DESTDIR="${pkgdir}"

  install -dm755 "$pkgdir/usr/share/licenses/$pkgname/"
  install -m644 ../OCCT_LGPL_EXCEPTION.txt "$pkgdir/usr/share/licenses/$pkgname"
}
