# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>
# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=python-ufonormalizer
_pyname=${pkgname#python-}
pkgver=0.6.3
pkgrel=1
pkgdesc='A tool that will normalize XML and other data inside of a UFO'
arch=(any)
url="https://github.com/unified-font-object/ufoNormalizer"
license=(BSD-3-Clause)
depends=(python)
makedepends=(python-{build,installer,wheel}
             python-setuptools-scm)
checkdepends=(python-pytest)
_archive="$_pyname-$pkgver"
source=("https://files.pythonhosted.org/packages/source/${_pyname::1}/$_pyname/$_archive.tar.gz")
sha256sums=('c3271097aba9d290594b75c2b432cf681088b74fe3eb334ca4319324e2bddd4e')

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
	pytest
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
	install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE.txt
}
