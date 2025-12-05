# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=py-geth
pkgname=python-${_name}
pkgver=6.4.0
pkgrel=1
pkgdesc="Python wrapping for running Go-Ethereum as a subprocess"
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(go-ethereum python python-pydantic python-requests python-semantic-version python-typing_extensions)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-flaky)
source=(${_name}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('d65a6353d6c66d66c70b9f5e6ceef71507c546cc5f042e4c0a28c8cff5d3d610e7f8b35417bdd943e1f53d2a3e6d2e787258529a4a3396da475bc32bd2654125')

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
