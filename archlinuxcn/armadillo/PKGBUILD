# Maintainer: Joey Dumont <joey.dumont@gmail.com>
# Contributor: Lucas Hermann Negri <lucashnegri at gmail dot com>
pkgname=armadillo
pkgver=10.6.1
_pkgver=${pkgver/_/-} # For use with RC releases, to replace the _ with -

pkgrel=1
pkgdesc="C++ linear algebra library"
arch=('i686' 'x86_64')
url="http://arma.sourceforge.net/"
license=('Apache')
depends=('lapack' 'blas' 'arpack' 'superlu>=5.2.0')
optdepends=('hdf5: HDF5 output'
            'intel-mkl: Intel Math Kernel Library support')
makedepends=('cmake')
source=("http://downloads.sourceforge.net/sourceforge/arma/$pkgname-$_pkgver.tar.xz")
install=armadillo.install
sha512sums=('648402e15c28a1b89bf08329e67d2549b72a203416fdf31fc792984c2f76f4b143afa36afa94293eed774fc4d5c033dd052d3e291ef810529c8096b6dc3fac1f')

build() {
  if [ "$CARCH" == "x86_64" ]; then
    ARMA64LIBDIR="-DINSTALL_LIB_DIR:PATH=/usr/lib"
  fi

  cd "${srcdir}/$pkgname-$_pkgver"
  cmake $ARMA64LIBDIR -DCMAKE_INSTALL_PREFIX:PATH=/usr .
  make
}

package() {
  cd "${srcdir}/$pkgname-$_pkgver"
  make DESTDIR="${pkgdir}" install
  install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
