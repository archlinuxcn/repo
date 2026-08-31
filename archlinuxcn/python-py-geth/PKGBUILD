# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=py-geth
pkgname=python-${_name}
pkgver=7.0.1
pkgrel=2
pkgdesc="Python wrapping for running Go-Ethereum as a subprocess"
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(go-ethereum python python-pydantic python-requests python-semantic-version python-typing_extensions)
makedepends=(git python-build python-installer python-setuptools python-setuptools-scm python-wheel)
checkdepends=(go python-pytest python-flaky)
source=(git+$url.git#tag=v$pkgver)
sha512sums=('e83d4c90d897c3a9f32a38456bbba36e987b20365d36718374f9a4c351d111b2a456341704a4dc931a420bda9580390aa6e5e4dacd8fd3178cd73ff54ff915c8')

build() {
  cd $_name
  python -m build --wheel --no-isolation
}

check() {
  cd $_name
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest -vv --showlocals tests/
}

package() {
  cd $_name
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
