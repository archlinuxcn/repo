# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>
# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=python-ufonormalizer
_pyname=${pkgname#python-}
pkgver=0.6.1
pkgrel=3
pkgdesc='A tool that will normalize XML and other data inside of a UFO'
arch=(any)
url="https://github.com/unified-font-object/ufoNormalizer"
license=(BSD)
depends=(python)
makedepends=(python-{build,installer,wheel}
             python-setuptools-scm)
_archive="$_pyname-$pkgver"
source=("https://files.pythonhosted.org/packages/source/${_pyname::1}/$_pyname/$_archive.zip")
sha256sums=('e61110e75a500083f265385b1354b578610f9542e3bbbeedb98a2a6155e4aa6c')

prepare() {
	cd "$_archive"
	# Upstream Issue: https://github.com/unified-font-object/ufoNormalizer/issues/87
	sed -i -e 's/ "wheel",//' pyproject.toml
}

build() {
	cd "$_archive"
	python -m build -wn
}

check() {
	cd "$_archive"
	export PYTHONPATH="$PWD/build/lib"
	python -m unittest discover
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
	install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE.txt
}
