# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=eth-bloom
pkgname=python-${_name}
pkgver=3.1.0
pkgrel=1
pkgdesc="An implementation of the Ethereum bloom filter."
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-eth-hash)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-hypothesis)
source=(${_name}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('94b93373002424219fad348259aa426e008c723c09286a1f821ea23f2eb21869dcf6f605ed365d282aa1ad316242d6b154e817941b6a31cfbd70c8ec16b8eeb1')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
}

check(){
  cd $_name-$pkgver
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest -vv --showlocals tests/
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
