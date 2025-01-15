# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=py-geth
pkgname=python-${_name}
pkgver=5.2.0
pkgrel=1
pkgdesc="Python wrapping for running Go-Ethereum as a subprocess"
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(go-ethereum python python-pydantic python-requests python-semantic-version python-typing_extensions)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-flaky)
source=(${_name}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('e6c8648ec05ebd91730e54a303c2f256f6072c5b51e25d3e413ef39e43e93d12970c244214602f51cdb79a2f920b8e2ce3f1338d0048c763423e4f7e45284b39')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
}

check(){
  cd $_name-$pkgver
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest -vv --showlocals tests/
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
