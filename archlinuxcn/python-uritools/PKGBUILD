# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=uritools
pkgname=python-$_name
pkgver=6.1.3
pkgrel=2
pkgdesc="URI parsing, classification and composition"
arch=(any)
url="https://github.com/tkem/$_name"
license=(MIT)
depends=(python)
makedepends=(python-build python-installer python-setuptools python-wheel python-setuptools-scm)
checkdepends=(python-pytest)
source=($pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz)
sha512sums=('2e168331796a3545bcb39d8e26a91039ff566d8fb4faf6fe7255762bb940e3134cc1a3bbb380e8611139c260879baa332b1253544d178227e763360c2997f582')

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
