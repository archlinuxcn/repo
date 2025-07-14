# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=web3.py
pkgname=python-web3
pkgver=7.12.1
pkgrel=1
pkgdesc="A python interface for interacting with the Ethereum blockchain and ecosystem."
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-eth-abi python-eth-account python-eth-keys python-eth-typing python-eth-utils python-hexbytes python-aiohttp python-pydantic python-requests python-typing_extensions python-websockets python-pyunormalize python-toolz python-rlp python-idna)
makedepends=(python-build python-installer python-setuptools python-wheel python-sphinx python-sphinx_rtd_theme)
#checkdepends=(python-pytest python-pytest-asyncio python-flaky python-eth-tester python-hypothesis python-py-geth)
source=(${_name}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('b7f4c50248f757f44df4942aeff54871b65552864a039fb442bbcf5ff21911e7e032644aa5349f1060993d150f37278f0c64e70b06b150571533bca05afa8f2c')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
  make -C docs man
}

# Very slow
# check()
#   cd $_name-$pkgver
#   python -m venv --system-site-packages test-env
#   test-env/bin/python -m installer dist/*.whl
#   test-env/bin/python -m pytest -vv --showlocals tests/
# }

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 docs/_build/man/web3.1 -t "$pkgdir/usr/share/man/man1"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
