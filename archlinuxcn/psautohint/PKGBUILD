# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Mark Wagie <mark dot wagie at tutanota dot com>

pkgname=psautohint
pkgver=2.4.0
pkgrel=2
epoch=3
pkgdesc='A standalone version of AFDKO’s autohinter'
arch=(x86_64)
url="https://github.com/adobe-type-tools/$pkgname"
license=(Apache)
_py_deps=(fonttools
          fs
          lxml)
depends=(python
         "${_py_deps[@]/#/python-}")
makedepends=(python-{build,installer,wheel}
             python-setuptools-scm)
_archive="$pkgname-$pkgver"
source=("https://pypi.org/packages/source/${pkgname:0:1}/$pkgname/$_archive.tar.gz")
sha256sums=('d50edea8f6121c3383f0d82f881bf7a18bdd476cc2d354737672ce193c3cff7f')

build() {
	cd "$_archive"
	python -m build -wn
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
	install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE
}
