# Maintainer: Nicola Revelant <nicolarevelant@outlook.com>
# Contributor: jelle van der Waa <jelle@vdwaa.nl>
# Contributor: Felix Kaiser <felix.kaiser@fxkr.net>

pkgname=python-mock
pkgver=5.2.0
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
b2sums=('5f936866cb0cffafadf4320b50e43e60bf84ccef80a5858ce6cd0d2569050b379de86979b52bff6d44f068a29e86b49e63f480a1f883b9650d11bb340e3ce5f7')

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
