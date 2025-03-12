# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=certvalidator
pkgname=python-pyhanko-${_name}
pkgver=0.26.7
pkgrel=1
pkgdesc="Python library for validating X.509 certificates and paths"
arch=(any)
url="https://github.com/MatthiasValvekens/${_name}"
license=(MIT)
depends=(python python-asn1crypto python-oscrypto python-cryptography python-uritools python-requests python-aiohttp)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-freezegun python-pytest-asyncio)
source=(${_name}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('9daf49a3822ec33853737f80cd7b32fea2635697c4031b6f5556adbc86ab6b3867a750e9bdba36bf9d8f486b7bdf15a09bed2c4fc225cf3122a17edeb13b4bc0')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
}

check(){
  cd $_name-$pkgver
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest -vv tests
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
