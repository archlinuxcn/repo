# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=eth-rlp
pkgname=python-${_name}
pkgver=2.1.0
pkgrel=1
pkgdesc="RLP definitions for common Ethereum objects in Python"
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-eth-utils python-hexbytes python-rlp)
makedepends=(python-build python-installer python-setuptools python-wheel python-sphinx python-sphinx_rtd_theme)
checkdepends=(python-pytest)
source=(${_name}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('c55490aadc80d5b5aba6f53c7230ba5caaae94ed0850f0be59d39589e1df3c97085a65d967601c7f99d03910b8f8b526d2aebf4966e10d50cfe2a559d37aa066')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
  make -C docs man
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
  install -Dm644 docs/_build/man/eth_rlp.1 -t "$pkgdir/usr/share/man/man1"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
