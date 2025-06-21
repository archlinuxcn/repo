# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=python-browserstack-local
_pkgname=browserstack-local
pkgver=1.2.12
pkgrel=1
pkgdesc='Python bindings for BrowserStack Local'
arch=(any)
url="http://github.com/browserstack/$_pkgname-python"
license=(MIT)
depends=(python
         python-psutil)
makedepends=(python-{build,installer,wheel}
             python-setuptools)
_archive="$_pkgname-$pkgver"
source=("https://files.pythonhosted.org/packages/source/${_pkgname::1}/$_pkgname/$_archive.tar.gz")
sha256sums=('7f890ec69d93a54336395d71f9b426d6cf46764bd013ddb9c6650e0b63883011')

build() {
	cd "$_archive"
	python -m build -wn
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
}
