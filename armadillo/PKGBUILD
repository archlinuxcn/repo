# Maintainer: Joey Dumont <joey.dumont@gmail.com>
# Contributor: Lucas Hermann Negri <lucashnegri at gmail dot com>

pkgname=armadillo
pkgver=6.700.3
pkgrel=1
pkgdesc="C++ linear algebra library"
arch=('i686' 'x86_64')
url="http://arma.sourceforge.net/"
license=('MPL 2.0')
depends=('lapack' 'blas' 'arpack' 'superlu=4.3')
optdepends=('hdf5: HDF5 output'
            'cuda: NVBLAS support'
	    'acml-cblas: ACML support')
makedepends=('cmake')
source=("http://downloads.sourceforge.net/sourceforge/arma/$pkgname-$pkgver.tar.gz")
install=armadillo.install
sha512sums=('89d25e5e1301ad954ba22689d825724d7c8b472d831b08a75a1d23968fb11e41b56f6a9c160dfc4433aebcc5d79851ab6352843bb7d580c74f06f3329638d8c8')

build() {
  if [ "$CARCH" == "x86_64" ]; then
    ARMA64LIBDIR="-DINSTALL_LIB_DIR:PATH=/usr/lib"
  fi

  cd "${srcdir}/$pkgname-$pkgver"
  cmake  $ARMA64LIBDIR -DCMAKE_INSTALL_PREFIX:PATH=/usr .
  make
}

package() {
  cd "${srcdir}/$pkgname-$pkgver"
  make DESTDIR="${pkgdir}" install
  install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
      
