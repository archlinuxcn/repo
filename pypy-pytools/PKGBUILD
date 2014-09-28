# $Id: PKGBUILD 108485 2014-03-27 14:48:16Z fyan $
# Maintainer: Felix Yan <felixonmars@gmail.com>
# Contributor: Stéphane Gaudreault <stephane@archlinux.org>

pkgbase=pypy-pytools
pkgname=('pypy3-pytools' 'pypy-pytools')
pkgver=2014.3
pkgrel=2
pkgdesc="A collection of tools for Python"
arch=('any')
url="http://mathema.tician.de/software/pytools"
license=('MIT')
makedepends=('pypy-setuptools' 'pypy3-setuptools')
source=(http://pypi.python.org/packages/source/p/pytools/pytools-${pkgver}.tar.gz)
sha512sums=('8c94e185ff6f22b2051518d209373db92d2c9f993e3de803928f588a43d893259bdc378b0d65faef27301aa794c7d86afeea8cf055e19401182f87bd119af137')

build() {
   cp -a pytools-${pkgver}{,-python2}

   cd "$srcdir/pytools-${pkgver}"
   pypy3 setup.py build

   cd "${srcdir}/pytools-${pkgver}-python2"
   pypy setup.py build
}

package_pypy-pytools() {
   depends=('pypy' 'pypy-decorator')
   cd "${srcdir}/pytools-${pkgver}-python2"
   pypy setup.py install --root="${pkgdir}" --skip-build --optimize=1
}

package_pypy3-pytools(){
   depends=("pypy3>=2.3" "pypy3<2.4" 'pypy3-decorator')
   cd "${srcdir}/pytools-${pkgver}"
   pypy3 setup.py install --root="${pkgdir}" --skip-build --optimize=1
}
