# Maintainer: Kewl <xrjy@nygb.rh.bet(rot13)>

pkgname='python-inform'
_pkgname=${pkgname#python-}
pkgver=1.34
pkgrel=1
pkgdesc="Print and logging utilities for communicating with user"
arch=('any')
depends=(python-six python-arrow)
makedepends=(python-build python-installer python-flit-core)
url="https://github.com/KenKundert/$_pkgname"
license=('GPL3')
source=("https://files.pythonhosted.org/packages/source/${_pkgname::1}/$_pkgname/$_pkgname-$pkgver.tar.gz")
sha256sums=('c463106e1b14b8719e168ec39d0efd736d2be082edc46e1f59f95fdc6d02f2b7')

build() {
    cd "$_pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$_pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
