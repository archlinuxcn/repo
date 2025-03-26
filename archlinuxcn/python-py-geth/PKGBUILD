# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=py-geth
pkgname=python-${_name}
pkgver=5.3.0
pkgrel=1
pkgdesc="Python wrapping for running Go-Ethereum as a subprocess"
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(go-ethereum python python-pydantic python-requests python-semantic-version python-typing_extensions)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-flaky)
source=(${_name}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('f98848e7f8f5773ec54da752b658c08d6c2478e295dcedf685daf826282c94f4b002d806c3fd200aa762c868f308e3f19b51a1a930461889716b7c0401997687')

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
