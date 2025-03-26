# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=uritools
pkgname=python-$_name
pkgver=4.0.3
pkgrel=3
pkgdesc="URI parsing, classification and composition"
arch=(any)
url="https://github.com/tkem/$_name"
license=(MIT)
depends=(python)
makedepends=(python-build python-installer python-setuptools python-wheel python-sphinx)
checkdepends=(python-pytest)
source=($pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz)
sha512sums=('cf075e60544a4638dbb648062b4d9fc879ccd0a609dc353fb3b73defc42ab38bf03d8baca47e7d3128c0f4ff58352854f39674fa5aa3a57cc121e021d3e0bd47')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
  make -C docs man
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
