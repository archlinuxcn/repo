# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=trie
pkgname=python-${_name}
pkgver=3.1.0
pkgrel=1
pkgdesc="Python library which implements the Ethereum Trie structure."
arch=(any)
url="https://github.com/ethereum/py-trie"
license=(MIT)
depends=(python python-eth-hash python-eth-typing python-eth-utils python-hexbytes python-rlp python-sortedcontainers)
makedepends=(git python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-hypothesis)
source=(git+$url.git#tag=v$pkgver
        git+https://github.com/ethereum/tests.git)
sha512sums=('cb4a5036f40e3e980f5fc18f74a46f1efc3b84710cf6e2b2c69d5255039e716756b99776178de242bfd7a88c7dcf1ee13dc20c71c02b976af0607b5ab1b351bb'
            'SKIP')

prepare() {
  cd py-trie
  git config --global protocol.file.allow always
  git submodule init fixtures
  git config submodule.fixtures.url ../tests
  git submodule update fixtures
}

build() {
  cd py-trie
  python -m build --wheel --no-isolation
}

check(){
  cd py-trie
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest -vv --showlocals tests/
}

package() {
  cd py-trie
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
