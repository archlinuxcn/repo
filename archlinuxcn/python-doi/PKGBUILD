# Maintainer: Gesh <gesh@gesh.uni.cx>
# Contributor: JP-Ellis <josh@jpellis.me>

pkgname=python-doi
_name=${pkgname}
pkgver=0.2.0
pkgrel=4
pkgdesc="Python package to work with Document Object Identifier (doi)."
arch=('any')
url="https://pypi.org/project/python-doi"
license=('GPL-3.0-or-later')
makedepends=(python-build python-installer python-wheel python-setuptools)
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('2e01e56fb319bd219ea8586baa43a1fc794dfe45a83156ac70242c4ce961fd9a')

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
