# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=near-sdk-py
pkgname=python-$_name
pkgver=0.7.3
pkgrel=1
pkgdesc="A Pythonic interface for building NEAR smart contracts"
arch=(any)
url="https://github.com/r-near/$_name"
license=(MIT)
depends=(python)
makedepends=(python-build python-installer python-wheel python-hatchling)
checkdepends=(python-pytest)
source=($_name-$pkgver.tar.gz::${url}/archive/v$pkgver.tar.gz)
sha512sums=('27766145617eb3dec3beb921d3126f456d8c68b5203a1eafaed229872d711f910855ab24885261e37cff8cb29e0dfe7a86d274da8f65f816dce6b2ad0d10da87')

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
  # Newly added, uncomment on next upstream release
  # install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
  cp -r docs "$pkgdir/usr/share/doc/$pkgname"
}
