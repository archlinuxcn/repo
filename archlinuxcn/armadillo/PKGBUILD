# Maintainer: Joey Dumont <joey.dumont@gmail.com>
# Contributor: Lucas Hermann Negri <lucashnegri at gmail dot com>
pkgname=armadillo
pkgver=9.400.4
_pkgver=9.400.4                     # For use with RC releases, to replace the - with _
pkgrel=1
pkgdesc="C++ linear algebra library"
arch=('i686' 'x86_64')
url="http://arma.sourceforge.net/"
license=('Apache')
depends=('lapack' 'blas' 'arpack' 'superlu>=5.2.0')
optdepends=('hdf5: HDF5 output'
            'cuda: NVBLAS support'
	    'acml-cblas: ACML support')
makedepends=('cmake')
source=("http://downloads.sourceforge.net/sourceforge/arma/$pkgname-$_pkgver.tar.xz")
install=armadillo.install
sha512sums=('f4f242b6be9a200c3f91d5288f617ae63667d42c6a36a5dedf66484e7bee96ff0d33efeec6c99a25efbedec8495ffa7ed5e4a91db5ac2585f73dbefb60e194f9')

build() {
  if [ "$CARCH" == "x86_64" ]; then
    ARMA64LIBDIR="-DINSTALL_LIB_DIR:PATH=/usr/lib"
  fi

  cd "${srcdir}/$pkgname-$_pkgver"
  cmake  $ARMA64LIBDIR -DCMAKE_INSTALL_PREFIX:PATH=/usr .
  make
}

package() {
  cd "${srcdir}/$pkgname-$_pkgver"
  make DESTDIR="${pkgdir}" install
  install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
      
