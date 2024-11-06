# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: William Turner <willtur.will@gmail.com>

pkgname=afdko
pkgver=4.0.2
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
             git # Upstream Issue: https://github.com/adobe-type-tools/afdko/issues/1407
             ninja
             python-{build,installer,wheel}
             python-scikit-build
             python-setuptools-scm)
checkdepends=(python-pytest)
conflicts=(spot-client)
_archive="$pkgname-$pkgver"
source=("$url/releases/download/$pkgver/$_archive.tar.gz")
sha256sums=('e1a31e871e83dd022635b852297c433c8e9c9d9d4f0c0f634e8d55dde28ad930')

prepare () {
	cd "$_archive"
	sed -i '/"wheel",/d;/"cmake",/d;/"ninja"/d;s/"scikit-build",/"scikit-build"/' pyproject.toml
	sed -i -e 's/==/>=/g;s/,<=[0-9.]\+//' requirements.txt
	sed -i -E "/'(wheel|cmake|ninja)',?$/d" setup.py
}

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
