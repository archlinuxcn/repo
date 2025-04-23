# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=py-evm
pkgname=python-${_name}
pkgver=0.12.0b2
pkgrel=1
pkgdesc="A Python implementation of the Ethereum Virtual Machine"
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-cached-property python-eth-bloom python-eth-hash python-eth-keys python-eth-typing python-eth-utils python-lru-dict python-py_ecc python-rlp python-trie python-ckzg python-toolz python-pycryptodome)
makedepends=(python-build python-installer python-setuptools python-wheel)
# hyphen in git tag, hard to automated upgrade
source=(https://files.pythonhosted.org/packages/source/${_name::1}/${_name//-/_}/${_name//-/_}-$pkgver.tar.gz)
sha512sums=('e926e05d0a97d341a0dd710a961aaaf77eda1f3aa319eb2bfb13be7a670753127305ceee16ec3b9ee96d300994382b67816084fb2fc748de131c6a6d013f4280')

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
