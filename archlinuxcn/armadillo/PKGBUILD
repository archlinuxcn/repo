# Maintainer: Joey Dumont <joey.dumont@gmail.com>
# Contributor: Lucas Hermann Negri <lucashnegri at gmail dot com>
pkgname=armadillo
pkgver=12.0.1
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
sha512sums=('b1b9fbce6bdacc3340ab190605aba77e821629e0a51e0c6277840eaf803d037a778b9243c02c5b55d67976c203808a5fc34894f3928b707685f6d8695ef0bc0d')

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
