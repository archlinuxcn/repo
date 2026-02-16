# Maintainer: Harriet O'Brien <harrietobrien@protonmail.com>
# Contributor: Achmad Fathoni<fathoni.id(at)gmail.com>
pkgname=python-pandas-stubs
_pkgname=pandas-stubs
pkgver=2.2.3.241126
pkgrel=1
pkgdesc="Type annotations for Pandas"
arch=('any')
url="https://github.com/pandas-dev/pandas-stubs"
license=('MIT')
makedepends=(python-build python-installer python-wheel python-poetry)
source=("${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('9037368ee8449dd01a5a94822e90fbdec3306edbb4298c49d5099d53e60cb504')

build() {
    cd $srcdir/$_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $srcdir/$_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
