# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=eth-rlp
pkgname=python-${_name}
pkgver=2.2.0
pkgrel=1
pkgdesc="RLP definitions for common Ethereum objects in Python"
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-eth-utils python-hexbytes python-rlp)
makedepends=(python-build python-installer python-setuptools python-wheel python-sphinx python-sphinx_rtd_theme)
checkdepends=(python-pytest)
source=(${_name}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('d89ba91e8345fdd30f72d70a0e3abd018c7abe1d8e7655f43ee858b2ab274079bc3dca5a9f9f9079b3df9b19b25d2a0987751e65b7a6dd83ea4407f47d2e5285')

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
