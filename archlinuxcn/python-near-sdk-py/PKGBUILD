# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=near-sdk-py
pkgname=python-$_name
pkgver=1.0.0
pkgrel=1
pkgdesc="A Pythonic interface for building NEAR smart contracts"
arch=(any)
url="https://github.com/r-near/$_name"
license=(MIT)
depends=(python)
makedepends=(python-build python-installer python-wheel python-hatchling)
checkdepends=(python-pytest)
source=($_name-$pkgver.tar.gz::${url}/archive/v$pkgver.tar.gz)
sha512sums=('5712be7a5363264a3a8c88702e7bfbaa9fece5d8b6942bbd18c511278e0f8fb589506a82baab038d282bb224f3bbc0504fabe7336e4b24e31281e64689340428')

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
