# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=eth-keyfile
pkgname=python-${_name}
pkgver=0.9.1
pkgrel=1
pkgdesc="Tools for handling the encrypted keyfile format used to store private keys."
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-pycryptodome python-eth-typing python-eth-keys python-eth-utils python-py_ecc)
makedepends=(git python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest)
source=(git+$url.git#tag=v$pkgver
        git+https://github.com/ethereum/tests.git)
sha512sums=('8e3d89ac5576113e189a01cd09975d7e3b0bcb4ab171eca34e2bd305633ced6f1aaf9c090e6491d8a86f541b0b61e73ddcf6aaec9fae02a0ffe28209ade61658'
            'SKIP')

prepare() {
  cd $_name
  git config --global protocol.file.allow always
  git submodule init fixtures
  git config submodule.fixtures.url ../tests
  git submodule update fixtures
}

build() {
  cd $_name
  python -m build --wheel --no-isolation
}

check(){
  cd $_name
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest -vv --showlocals tests/
}

package() {
  cd $_name
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm 644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
