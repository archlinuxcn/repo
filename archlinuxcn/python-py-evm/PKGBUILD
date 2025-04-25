# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=py-evm
pkgname=python-${_name}
pkgver=0.12.0b3
pkgrel=1
pkgdesc="A Python implementation of the Ethereum Virtual Machine"
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-cached-property python-eth-bloom python-eth-hash python-eth-keys python-eth-typing python-eth-utils python-lru-dict python-py_ecc python-rlp python-trie python-ckzg python-toolz python-pycryptodome)
makedepends=(python-build python-installer python-setuptools python-wheel)
# hyphen in git tag, hard to automated upgrade
source=(https://files.pythonhosted.org/packages/source/${_name::1}/${_name//-/_}/${_name//-/_}-$pkgver.tar.gz)
sha512sums=('e5afcfae6a38375d7dbc7a97e85e8d4ca971c64d64595171fac7b7426be33ed7c33ffa72106c48d2d67db07404e7f4449886446bac83a4525cce4b7ed9984fcb')

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
