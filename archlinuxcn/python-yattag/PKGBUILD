# Maintainer: Kyle Manna <kyle[at]kylemanna[d0t]com>

_pkgname=yattag
pkgname=python-${_pkgname}
pkgver=1.16.1
pkgrel=1
pkgdesc='Python library for generating HTML or XML in a pythonic way.'
url='http://yattag.org'
depends=('python')
makedepends=('python-build'
             'python-installer'
             'python-setuptools'
             'python-wheel')
license=('LGPL')
arch=('any')
source=("https://pypi.python.org/packages/source/y/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('baa8f254e7ea5d3e0618281ad2ff5610e0e5360b3608e695c29bfb3b29d051f4')

build() {
    cd "$srcdir/$_pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$srcdir/$_pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
    rm -rf ${pkgdir}/usr/lib/python3*/site-packages/tests/
}
