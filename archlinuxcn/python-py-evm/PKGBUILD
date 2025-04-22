# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=py-evm
pkgname=python-${_name}
pkgver=0.12.0b1
pkgrel=1
pkgdesc="A Python implementation of the Ethereum Virtual Machine"
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-cached-property python-eth-bloom python-eth-hash python-eth-keys python-eth-typing python-eth-utils python-lru-dict python-py_ecc python-rlp python-trie python-ckzg python-toolz python-pycryptodome)
makedepends=(python-build python-installer python-setuptools python-wheel)
# hyphen in git tag, hard to automated upgrade
source=(https://files.pythonhosted.org/packages/source/${_name::1}/${_name//-/_}/${_name//-/_}-$pkgver.tar.gz)
sha512sums=('3d9ec5d619391677bc084baf26a107f481fb0064b8f9a987ab744b1e66171c3e5849bce7a07f6eefa69a6122d2e502c403f1a19e581a3ee024706cdfd963e69a')

build() {
  cd ${_name//-/_}-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd ${_name//-/_}-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
