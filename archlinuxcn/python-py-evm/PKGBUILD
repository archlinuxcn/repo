# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=py-evm
pkgname=python-${_name}
pkgver=0.11.0b1
pkgrel=1
pkgdesc="A Python implementation of the Ethereum Virtual Machine"
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-cached-property python-eth-bloom python-eth-hash python-eth-keys python-eth-typing python-eth-utils python-lru-dict python-py_ecc python-rlp python-trie python-ckzg python-toolz python-pycryptodome)
makedepends=(python-build python-installer python-setuptools python-wheel)
# hyphen in git tag, hard to automated upgrade
source=(https://files.pythonhosted.org/packages/source/${_name::1}/${_name//-/_}/${_name//-/_}-$pkgver.tar.gz)
sha512sums=('a85e8989996f6465d9fd9d4ac6a1f94c5a4e0574f625306108545b5f3f89c2b88ea52193ae8601993cf1ebb06cea30ed88c2d4b959ccbb471eb094a5f19519cb')

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
