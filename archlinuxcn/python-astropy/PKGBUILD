# Contributor: Médéric Boquien <mboquien@free.fr>
# Maintainer: Médéric Boquien <mboquien@free.fr>
pkgname=python-astropy
pkgver=4.0.3
pkgrel=1
pkgdesc="A community python library for astronomy"
arch=('i686' 'x86_64')
url="http://www.astropy.org/"
license=('BSD')
depends=('python' 'python-numpy' 'python-scipy' 'python-h5py' 'cfitsio' 'expat' 'wcslib' 'erfa' 'python-jinja')
conflicts=('python-pyfits' 'python-vo')
makedepends=('cython' 'python-astropy-helpers')
source=("https://files.pythonhosted.org/packages/source/a/astropy/astropy-${pkgver}.tar.gz")
sha512sums=('a945b4b6161b96b552b3765b0009d1366b6841e811a4e6f526d264f7a13ba82d563ff497b3cbb49abe5f3ef0e9883c2720513027b26186c679ddeafb05ee1545')

prepare() {
  cd ${srcdir}/astropy-${pkgver}

  sed -i -e '/auto_use/s/True/False/' setup.cfg
}

build() {
  cd ${srcdir}/astropy-${pkgver}

  python setup.py build --use-system-libraries --offline
}

package() {
  cd ${srcdir}/astropy-${pkgver}

  install -d -m755 "${pkgdir}/usr/share/licenses/${pkgname}/"
  install -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}/" licenses/*
  python setup.py install --offline --root=${pkgdir} --prefix=/usr --optimize=1
}
