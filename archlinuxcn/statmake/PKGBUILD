# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=statmake
pkgver=1.0.0
pkgrel=1
pkgdesc='Dump, merge and compile Visual TrueType data in UFO3 with FontTools'
arch=(any)
url="https://github.com/daltonmaag/$pkgname"
license=(MIT)
_pydeps=(attrs
         cattrs
         fonttools
         fs) # for fonttools[ufo]
depends=(python
         "${_pydeps[@]/#/python-}")
makedepends=(python-{build,installer,wheel}
             python-hatchling
             python-hatch-vcs)
_archive="$pkgname-$pkgver"
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/$pkgname/$_archive.tar.gz")
sha256sums=('a0dc3b772ddb4f0811d1bd695ea6d4d4f20a2cb39a4e33338adc68201163f178')

build() {
	cd "$_archive"
	python -m build -wn
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
	install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE
}
