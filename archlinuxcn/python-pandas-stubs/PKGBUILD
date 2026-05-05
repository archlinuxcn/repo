# Maintainer: Harriet O'Brien <harrietobrien@protonmail.com>
# Contributor: Achmad Fathoni<fathoni.id(at)gmail.com>
pkgname=python-pandas-stubs
_pkgname=pandas-stubs
pkgver=3.0.0.260204
pkgrel=1
pkgdesc="Type annotations for Pandas"
arch=('any')
url="https://github.com/pandas-dev/pandas-stubs"
license=('MIT')
makedepends=(python-build python-installer python-wheel python-poetry-core)
source=("${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('359ed55ac1c610b1d1310e73e87f07f6beef7a28797abe0df1ec9377cc702a84')

build() {
    cd $srcdir/$_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $srcdir/$_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
