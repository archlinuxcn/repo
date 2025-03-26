# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=python-browserstack-local
_pkgname=browserstack-local
pkgver=1.2.10
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
sha256sums=('fb5d198e2b57e04085450fa2da0af00e47914a96f0b05fc302a8d8a7c48f5281')

build() {
	cd "$_archive"
	python -m build -wn
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
}
