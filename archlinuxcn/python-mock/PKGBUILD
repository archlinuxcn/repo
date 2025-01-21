# Maintainer: Nicola Revelant <nicolarevelant@outlook.com>
# Contributor: jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Felix Kaiser <felix.kaiser@fxkr.net>

pkgname=python-mock
pkgver=5.1.0
pkgrel=1
pkgdesc='Mocking and Patching Library for Testing'
url='https://mock.readthedocs.io/en/latest/'
depends=('python')
makedepends=(
	'python-build'
	'python-installer'
	'python-setuptools'
	'python-wheel'
)
checkdepends=('python-pytest')
license=('BSD-2-Clause')
arch=('any')
source=(mock-$pkgver.tar.gz::https://github.com/testing-cabal/mock/archive/$pkgver.tar.gz)
b2sums=('4dd8e69678424a0ea9c301e0b627ac7d981196f3deb4b622b0724896f10b0c1a84f28349f7fd27603f30c1470cf89f2436ff85195d3f42073d08f56076f9e9fd')

build() {
	cd "mock-$pkgver"
	python -m build --wheel --no-isolation
}

check() {
	cd "mock-$pkgver"
	echo 'python tests'
	python -m unittest discover
}

package() {
	cd "mock-$pkgver"
	python -I -m installer --destdir="$pkgdir" dist/*.whl
	install -Dm644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
