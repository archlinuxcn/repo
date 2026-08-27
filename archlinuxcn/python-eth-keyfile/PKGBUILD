# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=eth-keyfile
pkgname=python-${_name}
pkgver=0.10.0
pkgrel=2
pkgdesc="Tools for handling the encrypted keyfile format used to store private keys."
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-pycryptodome python-eth-typing python-eth-keys python-eth-utils python-py_ecc)
makedepends=(git python-build python-installer python-setuptools python-setuptools-scm python-wheel)
checkdepends=(python-pytest)
source=(git+$url.git#tag=v$pkgver
        git+https://github.com/ethereum/tests.git)
sha512sums=('8338e97b2f75dc39c405049c1b516e8f8edb18504dccfa613ad620bc21c32f4095ce0eed146b03d0429b895aaf478665c308d2c76a1ad2c5f6c9a7b428b95147'
            'SKIP')

prepare() {
  cd $_name
  git submodule init fixtures
  git config submodule.fixtures.url ../tests
  git -c protocol.file.allow=always submodule update fixtures
}

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
  install -Dm 644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm 644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
