# Maintainer: Joey Dumont <joey.dumont@gmail.com>
# Contributor: Lucas Hermann Negri <lucashnegri at gmail dot com>

pkgname=armadillo
pkgver=7.200.2
_pkgver=7.200.2
pkgrel=1
pkgdesc="C++ linear algebra library"
arch=('i686' 'x86_64')
url="http://arma.sourceforge.net/"
license=('MPL 2.0')
depends=('lapack' 'blas' 'arpack' 'superlu=5.2.0')
optdepends=('hdf5: HDF5 output'
            'cuda: NVBLAS support'
	    'acml-cblas: ACML support')
makedepends=('cmake')
source=("http://downloads.sourceforge.net/sourceforge/arma/$pkgname-$_pkgver.tar.xz")
install=armadillo.install
sha512sums=('c92747f256aec96da27f9dce2f33224883fccfc33b3be904d5de8ba52b540e3327f39b865f9547e06b437c9121a65ef42fe744f4319d518b44bc7795e489fc82')

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
      
