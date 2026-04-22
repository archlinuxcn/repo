# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=uritools
pkgname=python-$_name
pkgver=6.0.2
pkgrel=1
pkgdesc="URI parsing, classification and composition"
arch=(any)
url="https://github.com/tkem/$_name"
license=(MIT)
depends=(python)
makedepends=(python-build python-installer python-setuptools python-wheel python-sphinx)
checkdepends=(python-pytest)
source=($pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz)
sha512sums=('73b90566a6f908beb977500b9c60f1cb76e0de1ab26e4c422782ec0d6241361eb8761ee947b7168998e40d78b5247acd57bb75ab353c0c945eea9a7e6f04a772')

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
