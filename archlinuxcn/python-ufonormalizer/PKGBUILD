# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>
# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=python-ufonormalizer
_pyname=${pkgname#python-}
pkgver=0.6.2
pkgrel=2
pkgdesc='A tool that will normalize XML and other data inside of a UFO'
arch=(any)
url="https://github.com/unified-font-object/ufoNormalizer"
license=(BSD-3-Clause)
depends=(python)
makedepends=(python-{build,installer,wheel}
             python-setuptools-scm)
checkdepends=(python-pytest)
_archive="$_pyname-$pkgver"
source=("https://files.pythonhosted.org/packages/source/${_pyname::1}/$_pyname/$_archive.zip")
sha256sums=('4c5715bb948381f2c641af82b94938ad242d9b5365dd1c5b7ce3d75556a26c3a')

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
