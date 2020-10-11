# Contributor: Médéric Boquien <mboquien@free.fr>
# Maintainer: Médéric Boquien <mboquien@free.fr>
pkgname=python-astropy
pkgver=4.0.2
pkgrel=1
pkgdesc="A community python library for astronomy"
arch=('i686' 'x86_64')
url="http://www.astropy.org/"
license=('BSD')
depends=('python' 'python-numpy' 'python-scipy' 'python-h5py' 'cfitsio' 'expat' 'wcslib' 'erfa' 'python-jinja')
conflicts=('python-pyfits' 'python-vo')
makedepends=('cython' 'python-astropy-helpers')
source=("https://files.pythonhosted.org/packages/source/a/astropy/astropy-${pkgver}.tar.gz")
sha512sums=('0ca4829e147831a1d3fb87351b6b9fa294540b4777a3efc1cdc3a0921f236ca5229374a38b115cf0ff5573298d152af10531edef50708080a4761fa50edb8fcf')

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
