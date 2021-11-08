# Contributor: Médéric Boquien <mboquien@free.fr>
# Maintainer: Médéric Boquien <mboquien@free.fr>
pkgname=python-pyerfa
_name=${pkgname#python-}
pkgver=2.0.0.1
pkgrel=1
pkgdesc="Python wrapper for the ERFA library "
arch=('i686' 'x86_64')
url="https://github.com/liberfa/pyerfa"
license=('BSD')
depends=('python>=3.6' 'python-numpy>=1.16.0' 'erfa>=1.7.3')
makedepends=('cython' 'python-jinja' 'python-pip' 'python-setuptools-scm')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha512sums=('420e7bb2d00a9bd7d2290b6b0598b5963404ac021f713ae7bbf607135b9db6605f63dd89694d2cf406eb230b58b1028f2458f96ed834127ce9a398810cfea589')

build() {
  cd "${srcdir}/pyerfa-${pkgver}"

  PYERFA_USE_SYSTEM_LIBERFA=1 python setup.py build
}

package() {
  cd "${srcdir}/pyerfa-${pkgver}"

  install -d -m755 "${pkgdir}/usr/share/licenses/${pkgname}/"
  install -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}/" licenses/*
  PYTHONHASHSEED=0 python setup.py install --root="${pkgdir}/" --optimize=1 --skip-build
}
