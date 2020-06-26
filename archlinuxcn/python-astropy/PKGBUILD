# Contributor: Médéric Boquien <mboquien@free.fr>
# Maintainer: Médéric Boquien <mboquien@free.fr>
pkgname=python-astropy
pkgver=4.0.1
pkgrel=1
pkgdesc="A community python library for astronomy"
arch=('i686' 'x86_64')
url="http://www.astropy.org/"
license=('BSD')
depends=('python' 'python-numpy' 'python-scipy' 'python-h5py' 'cfitsio' 'expat' 'wcslib' 'erfa' 'python-jinja')
conflicts=('python-pyfits' 'python-vo')
makedepends=('cython' 'python-astropy-helpers')
source=("https://files.pythonhosted.org/packages/source/a/astropy/astropy-${pkgver}.tar.gz")
sha512sums=('523ca58830517ca478f1c0a57262936405a6b063d1ddf5c6c72da4324b5c398807941f90b9be9303f5fa6c1eb69c29fc288c86881deb8b8c44780f66890fe4b2')

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
