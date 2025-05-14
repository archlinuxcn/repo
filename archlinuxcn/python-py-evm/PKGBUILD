# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=py-evm
pkgname=python-${_name}
pkgver=0.12.1b1
pkgrel=1
pkgdesc="A Python implementation of the Ethereum Virtual Machine"
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-cached-property python-eth-bloom python-eth-hash python-eth-keys python-eth-typing python-eth-utils python-lru-dict python-py_ecc python-rlp python-trie python-ckzg python-toolz python-pycryptodome)
makedepends=(python-build python-installer python-setuptools python-wheel)
# hyphen in git tag, hard to automated upgrade
source=(https://files.pythonhosted.org/packages/source/${_name::1}/${_name//-/_}/${_name//-/_}-$pkgver.tar.gz)
sha512sums=('01a9a8729efd1a70cbe98e31eff6e8588f462ff0ea162058c4ffca1f50645de61faaa5dbc449e012ae30c8b95d763fba552e7d76d911a3b3d0e0e246e5e7d00c')

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
