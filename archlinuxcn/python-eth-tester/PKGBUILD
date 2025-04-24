# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=eth-tester
pkgname=python-${_name}
pkgver=0.13.0b1
pkgrel=1
pkgdesc="Tool suite for testing ethereum applications."
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-eth-abi python-eth-account python-eth-keys python-eth-typing python-eth-utils python-rlp python-semantic-version python-toolz python-hexbytes python-py-evm)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest)
# hyphen in git tag, hard to automated upgrade
source=(https://files.pythonhosted.org/packages/source/${_name::1}/${_name//-/_}/${_name//-/_}-$pkgver.tar.gz)
sha512sums=('05bee3741cb903e257cc6f6604d104081aae3697a1a06ea0e77f55876f6f33ae1feb0d574412b9cdf25033b4d4d64a658c1dd82dfcaa9f94824b1c016fc94359')

build() {
  cd ${_name//-/_}-$pkgver
  python -m build --wheel --no-isolation
}

check(){
  cd ${_name//-/_}-$pkgver
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest -vv --showlocals tests/
}

package() {
  cd ${_name//-/_}-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
