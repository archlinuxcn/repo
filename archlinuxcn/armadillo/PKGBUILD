# Maintainer: Joey Dumont <joey.dumont@gmail.com>
# Contributor: Lucas Hermann Negri <lucashnegri at gmail dot com>
pkgname=armadillo
pkgver=10.8.1
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
sha512sums=('96eb92b640078fb41ebb6cbcec2234cb5f23263933e00f3f42b002516e6f57a5cf3b874fa7197c7db89bc39e0a3a44c9c7b007af64486294d2e541386c6c232a')

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
