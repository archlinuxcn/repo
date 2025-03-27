# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=eth-account
pkgname=python-${_name}
pkgver=0.13.6
pkgrel=1
pkgdesc="Account abstraction library for web3.py"
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-bitarray python-eth-abi python-eth-keyfile python-eth-keys python-eth-rlp python-eth-typing python-eth-utils python-hexbytes python-rlp python-ckzg python-pydantic python-toolz)
makedepends=(python-build python-installer python-setuptools python-wheel python-sphinx python-sphinx_rtd_theme)
checkdepends=(python-pytest python-hypothesis nodejs npm)
source=(${_name}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('a0db31ed86eb5b8f436ee8403f4762141c10ca0c2a53a7921baa4a66800224db4d30c17436ee17fdfef771ba5e3705cf63634c75d19ad07002086c375bdb4329')

prepare() {
  cd $_name-$pkgver
  cd tests/integration/js-scripts
  npm ci
}

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
  install -Dm644 docs/_build/man/eth_account.1 -t "$pkgdir/usr/share/man/man1"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
