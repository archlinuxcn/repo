# Maintainer: Weirch Sodora <sodora at gmail dot com>

pkgbase=python-proboscis
pkgname=('python-proboscis' 'python2-proboscis')
pkgver=1.2.6.0
pkgrel=2
pkgdesc='Proboscis is a Python test framework that extends Python’s built-in unittest module and Nose with features from TestNG.'
arch=('any')
url='https://pypi.python.org/pypi/proboscis/'
license=('Apache')
makedepends=('python-setuptools' 'python2-setuptools')
source=("https://pypi.python.org/packages/3c/c8/c187818ab8d0faecdc3c16c1e0b2e522f3b38570f0fb91dcae21662019d0/proboscis-${pkgver}.tar.gz")
md5sums=('e4b36449ef7c18f70b8243f4c8bddbca')

prepare() {
    cd "${srcdir}"
    cp -a proboscis-${pkgver} proboscis-${pkgver}-py2
}

package_python-proboscis() {
    depends=('python')
    cd "${srcdir}/proboscis-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1
}

package_python2-proboscis() {
    depends=('python2')
    cd "${srcdir}/proboscis-${pkgver}-py2"
    python2 setup.py install --root="${pkgdir}" --optimize=1
}

