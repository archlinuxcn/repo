# $Id: PKGBUILD 142448 2015-10-01 16:05:48Z fyan $
# Maintainer: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Ralf Schmitt <ralf@systemexit.de>

_pkgbasename=python-greenlet
pkgname=libx32-python-greenlet
pkgver=0.4.9
pkgrel=2.1
pkgdesc="Lightweight in-process concurrent programming (x32 ABI)"
license=("MIT")
url="http://pypi.python.org/pypi/greenlet"
makedepends=('python-setuptools')
depends=('libx32-python' $_pkgbasename)
source=("https://pypi.python.org/packages/source/g/greenlet/greenlet-${pkgver}.zip")
arch=('x86_64')

build() {
	cd greenlet-$pkgver
	python-x32 setup.py build
}

check() {
    cd greenlet-$pkgver
    python-x32 setup.py test
}

package() {
    cd greenlet-$pkgver
    python-x32 setup.py install -O1 --root="$pkgdir"

    rm -rf "${pkgdir}"/usr/{share,libx32/python}
    mkdir -p "$pkgdir/usr/share/licenses"
    ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}

sha512sums=('2dce966827caf32b21cf005498ef6e595524ffb0aabbe424c705850986edfda4f4b2ba791180a7de900b1778594851de83a5b2cc69baf31c968ee8fb9131ba58')
