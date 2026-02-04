# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=web3.py
pkgname=python-web3
pkgver=7.14.1
pkgrel=1
pkgdesc="A python interface for interacting with the Ethereum blockchain and ecosystem."
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-eth-abi python-eth-account python-eth-keys python-eth-typing python-eth-utils python-hexbytes python-aiohttp python-pydantic python-requests python-typing_extensions python-websockets python-pyunormalize python-toolz python-rlp python-idna)
makedepends=(python-build python-installer python-setuptools python-wheel python-sphinx python-sphinx_rtd_theme)
#checkdepends=(python-pytest python-pytest-asyncio python-flaky python-eth-tester python-hypothesis python-py-geth)
source=(${_name}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('5a48cee213c085061ed63882ec1c1bea2e2cd71d66f3355f13c6a3d53c2e7b957b87fcd37c6708eab74abe83bf8c8602c68c35c0f421fa2f0fc326285c668813')

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
