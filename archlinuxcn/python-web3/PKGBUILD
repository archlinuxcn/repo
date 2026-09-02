# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=web3.py
pkgname=python-web3
pkgver=8.0.0
pkgrel=2
pkgdesc="A python interface for interacting with the Ethereum blockchain and ecosystem."
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-eth-abi python-eth-account python-eth-hash python-eth-keys python-eth-typing python-eth-utils python-hexbytes python-aiohttp python-pydantic python-requests python-typing_extensions python-websockets python-pyunormalize python-toolz python-rlp python-idna)
makedepends=(git python-build python-installer python-setuptools python-setuptools-scm python-wheel python-sphinx python-sphinx_rtd_theme)
checkdepends=(python-pytest python-pytest-asyncio python-pytest-mock python-flaky python-eth-tester python-hypothesis python-py-geth python-cached-property)
# Pin the geth binary to the version of tests/integration/geth-*-fixture.zip (CI GETH_VERSION).
_geth_ver=1.16.7
_geth_commit=b9f3a3d9
source=(git+$url.git#tag=v$pkgver
        https://gethstore.blob.core.windows.net/builds/geth-linux-amd64-$_geth_ver-$_geth_commit.tar.gz)
sha512sums=('8a875884a7c63655b7509d526680103a0b61a0bcdc55e210b78c56a34f57faf0c5b26c855f491dad7a06826aa23f10e12f556c56830777cb7a2621e606ba7d75'
            'e8e016044ce8cf73ba9a91377cb11703a5ba9c6cb89f67bdc31c1c063e1552d4bc0f80dcc84f8fbc6780be8d79287f0c22e3db01f4ee02faff399339257e050c')

build() {
  cd $_name
  python -m build --wheel --no-isolation
  python -m installer --destdir=tmp_install dist/*.whl
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  PYTHONPATH="$PWD/tmp_install$site_packages" make -C docs man
}

# Very slow
check() {
  cd $_name
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  # Beacon tests need a live consensus client; upstream CI does not run them.
  local pytest_args=(tests/core tests/ens tests/integration/test_ethereum_tester.py)
  # go-ethereum tests pin a geth fixture zip; use the matching official binary.
  local geth_bin="$srcdir/geth-linux-amd64-$_geth_ver-$_geth_commit/geth"
  if [[ -x $geth_bin ]]; then
    export GETH_BINARY=$geth_bin
    pytest_args+=(tests/integration/go_ethereum)
  fi
  test-env/bin/python -m pytest -vv --showlocals "${pytest_args[@]}"
}

package() {
  cd $_name
  python -m installer --destdir="$pkgdir" dist/*.whl
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir$site_packages"/docs
  install -Dm644 docs/_build/man/web3.1 -t "$pkgdir/usr/share/man/man1"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
