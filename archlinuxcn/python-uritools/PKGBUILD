# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=uritools
pkgname=python-$_name
pkgver=7.0.0
pkgrel=1
pkgdesc="URI parsing, classification and composition"
arch=(any)
url="https://github.com/tkem/$_name"
license=(MIT)
depends=(python)
makedepends=(python-build python-installer python-setuptools python-wheel python-setuptools-scm)
checkdepends=(python-pytest)
source=($pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz)
sha512sums=('c0371d88376205b3335675a7a5f29fc7a35389ad64b4c4b4460fc8f765050e2728e0ec8d5b20a6ffe1b50e282e146024239e905a38e57f8a31ec57b844450482')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
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
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.rst -t "$pkgdir/usr/share/doc/$pkgname"
}
