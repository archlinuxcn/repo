# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=uritools
pkgname=python-$_name
pkgver=6.0.1
pkgrel=1
pkgdesc="URI parsing, classification and composition"
arch=(any)
url="https://github.com/tkem/$_name"
license=(MIT)
depends=(python)
makedepends=(python-build python-installer python-setuptools python-wheel python-sphinx)
checkdepends=(python-pytest)
source=($pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz)
sha512sums=('959a78428825d19dcd2df0a958073c73f0c7508e8a57443efd78913e96fa2ccae1db717eecc1f7ca58de0690a175989b319d8b59871f56f205c97eb4428f5d01')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
  sphinx-build -b man docs/ docs/_build/man/
}

check(){
  cd $_name-$pkgver
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest -vv tests/
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 docs/_build/man/$_name.1 -t "$pkgdir/usr/share/man/man1"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.rst -t "$pkgdir/usr/share/doc/$pkgname"
}
