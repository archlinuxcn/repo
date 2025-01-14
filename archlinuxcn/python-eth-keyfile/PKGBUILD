# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=eth-keyfile
pkgname=python-${_name}
pkgver=0.8.1
pkgrel=2
pkgdesc="Tools for handling the encrypted keyfile format used to store private keys."
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-pycryptodome python-eth-typing python-eth-keys python-eth-utils)
makedepends=(git python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest)
source=($_name-$pkgver::git+https://github.com/ethereum/eth-keyfile.git#tag=v$pkgver
        git+https://github.com/ethereum/tests.git)
sha512sums=('3783406d0a41a7db3a75ecb2727644258a6d8f20f8310d567ee511af6e970d76ef6308a7c2d681ae967c5d8d1a39e1ab10b2d1a871c4a69b2a4c1d06a82dea56'
            'SKIP')

prepare() {
  cd $_name-$pkgver
  git config --global protocol.file.allow always
  git submodule init fixtures
  git config submodule.fixtures.url ../tests
  git submodule update fixtures
}

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
  install -Dm 644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm 644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
