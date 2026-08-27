# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=py-geth
pkgname=python-${_name}
pkgver=7.0.0
pkgrel=2
pkgdesc="Python wrapping for running Go-Ethereum as a subprocess"
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(go-ethereum python python-pydantic python-requests python-semantic-version python-typing_extensions)
makedepends=(git python-build python-installer python-setuptools python-setuptools-scm python-wheel)
checkdepends=(python-pytest python-flaky)
source=(git+$url.git#tag=v$pkgver)
sha512sums=('f0ca7bea3ed4a7b1bc8800e1f129cc05b246282ff9577148bec9ce25ea1488e534715dd4826f5cd2b54be1ef860a2f07c06af9735fb2b727ab7ea78e4a2cd3ee')

build() {
  cd $_name
  python -m build --wheel --no-isolation
}

check() {
  cd $_name
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest -vv --showlocals tests/
}

package() {
  cd $_name
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
