# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=eth-tester
pkgname=python-${_name}
pkgver=0.14.0b1
pkgrel=2
pkgdesc="Tool suite for testing ethereum applications."
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-eth-abi python-eth-account python-eth-keys python-eth-typing python-eth-utils python-rlp python-semantic-version python-toolz python-hexbytes python-py-evm)
makedepends=(git python-build python-installer python-setuptools python-setuptools-scm python-wheel)
checkdepends=(python-pytest)
# PyPI: 0.14.0b1; git tag: v0.14.0-beta.1
source=(git+$url.git#tag=v${pkgver/b/-beta.})
sha512sums=('6b21d85f005dd445878e553ddd636bbc3ad8ec0fcf95f3eb5f49b27d972e08b9d593cf1f66b47e608ed2b0e703dae76bbd5853d0b94c7baa0c415bd0354da30d')

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
