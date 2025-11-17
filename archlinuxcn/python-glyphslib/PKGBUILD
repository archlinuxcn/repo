# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>

_pyname=glyphsLib
pkgname=python-${_pyname,,}
pkgver=6.12.4
pkgrel=1
pkgdesc='A bridge from Glyphs source files (.glyphs) to UFOs'
arch=(any)
url="https://github.com/googlefonts/$_pyname"
license=(Apache-2.0)
_pydeps=(fonttools
         fs # for fonttools[ufo]
         openstep-plist
         ufolib2
         unicodedata2) # for fonttools[unicode]
depends=(python
         "${_pydeps[@]/#/python-}")
makedepends=(python-{build,installer,wheel}
             python-defcon
             python-setuptools-scm)
_pycheckdeps=(lxml # for fonttools[lxml]
              pytest
              ufo2ft
              ufonormalizer)
checkdepends=("${_pycheckdeps[@]/#/python-}"
              xmldiff)
optdepends=(python-defcon
            python-ufonormalizer)
_archive="${_pyname,,}-$pkgver" # upstream goes back and forth on casing of sdist
source=("https://files.pythonhosted.org/packages/source/${_pyname::1}/$_pyname/$_archive.tar.gz")
sha256sums=('5e5144b84ce7619c8cf7e0937d39dfc1b6808e2ebe455a7c32ee1a91cf57907d')

build() {
	cd "$_archive"
	python -m build -wn
}

check() {
	cd "$_archive"
	# skipped interpolation and designspace tests assume pinned version of defcon, Arch's might be newer
	# skipped builder test requires ufo2ft, a circular dependency which might be older version than expected
	# skipped tests expecting output of old version of ufoLib2
	PYTHONPATH=Lib pytest tests \
		--deselect tests/builder/interpolation_test.py \
		--deselect tests/builder/designspace_gen_test.py \
		--deselect tests/builder/builder_test.py \
		--deselect tests/builder/to_glyphs_test.py
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
}
