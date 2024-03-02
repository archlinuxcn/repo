# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=statmake
pkgver=0.6.0
pkgrel=2
pkgdesc='Dump, merge and compile Visual TrueType data in UFO3 with FontTools'
arch=(any)
url="https://github.com/daltonmaag/$pkgname"
license=(MIT)
_py_deps=(attrs
          cattrs
          fonttools
          fs) # optdepends of fonttools required for [ufo]
depends=(python
         "${_py_deps[@]/#/python-}")
makedepends=(python-{build,installer,wheel}
             python-poetry)
_archive="$pkgname-$pkgver"
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/$pkgname/$_archive.tar.gz")
sha256sums=('b3353ddc344fc8013960c6f45565f701ffe7cfbfb7ec91a69020945371fc486c')

build() {
	cd "$_archive"
	python -m build -wn
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
	install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE
}
