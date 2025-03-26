# Maintainer: Caleb Maclennan <caleb@alerque.com>

_pyname=plum
pkgname=python-${_pyname,,}
pkgver=0.8.7
pkgrel=3
pkgdesc='Pack/Unpack Memory'
arch=(any)
url="https://$_pyname-py.readthedocs.io/en/latest/"
license=(MIT)
depends=(python)
makedepends=(python-{build,installer,wheel}
             python-setuptools)
_archive="$_pyname-$pkgver"
source=("https://gitlab.com/dangass/$_pyname/-/archive/$pkgver/$_archive.tar.bz2")
sha256sums=('d0e0a40ac106260ce820018e22ef0cdcc569b267de51e667585b87f4215c2cd8')

prepare() {
	cd "$_archive"
	sed -i -e '/python_requires/d' setup.cfg
}

build() {
	cd "$_archive"
	python -m build -wn
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
}
