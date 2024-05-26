# Maintainer: JP-Ellis <josh@jpellis.me>
# Contributor: Francois Boulogne <fboulogne at april dot org>
pkgname=python-arxiv2bib
_name=${pkgname#python-}
pkgver=1.0.8
pkgrel=1
pkgdesc="Provides a command line tool to get metadata for an academic paper posted at arXiv.org in BibTeX format."
arch=('any')
url="https://pypi.org/project/arxiv2bib"
license=('BSD')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('137608ed8aa4da6594350152964b9b0f46c6efcb07f8a4dfd50309c968b647a8')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py build
  touch Changelog.rst
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
}

# vim:ts=2:sw=2:et:
