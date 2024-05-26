# Maintainer: JP-Ellis <josh@jpellis.me>
# Contributor: Francois Boulogne <fboulogne at april dot org>

pkgname=python-bibtexparser
_name=${pkgname#python-}
pkgver=1.4.1
pkgrel=2
pkgdesc="Bibtex parser in Python"
arch=('any')
url="https://pypi.org/project/bibtexparser/"
license=('LGPL3')
depends=('python' 'python-pyparsing')
makedepends=('python-setuptools')
checkdepends=('python-nose')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('e00e29e24676c4808e0b4333b37bb55cca9cbb7871a56f63058509281588d789')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py build
  touch Changelog.rst
}

check() {
  cd "${srcdir}/${_name}-${pkgver}"
  nosetests3
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}

# vim:ts=2:sw=2:et:
