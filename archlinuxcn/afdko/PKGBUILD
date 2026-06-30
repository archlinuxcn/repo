# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: William Turner <willtur.will@gmail.com>

pkgname=afdko
pkgver=5.0.1
pkgrel=1
pkgdesc='Adobe Font Development Kit for OpenType'
arch=(x86_64)
url="https://github.com/adobe-type-tools/$pkgname"
license=(Apache-2.0)
_pydeps=(booleanoperations
         brotli # for fonttools[woff]
         defcon
         fontmath
         fontpens # for defcon[pens]
         fonttools
         fs # for fonttools[ufo]
         lxml # for defcon[lxml] and fonttools[lxml]
         tqdm
         ufonormalizer
         ufoprocessor
         unicodedata2 # for fonttools[unicode]
         zopfli) # for fonttools[woff]
depends=(gcc-libs
         glibc
         libxml2
         python
         "${_pydeps[@]/#/python-}")
makedepends=(cmake
             cython
             git # Upstream Issue: https://github.com/adobe-type-tools/afdko/issues/1407
             ninja
             python-{build,installer,wheel}
             python-scikit-build-core
             python-setuptools-scm)
checkdepends=(python-pytest)
conflicts=(spot-client)
_archive="$pkgname-$pkgver"
source=("$url/releases/download/$pkgver/$_archive.tar.gz")
sha256sums=('083b504a1cd865e8bfbb42134a34318ce42ef5130daebfc5b0e2f2fb444326c5')

build() {
	cd "$_archive"
	python -m build -wn
}

check() {
	cd "$_archive"
	# Upstream test suite uses vendored deps and the paths are foobared
	# PYTHONPATH=python pytest
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
	install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE.md
}
