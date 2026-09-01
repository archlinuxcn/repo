# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=pyhanko_certvalidator
pkgname=python-pyhanko-certvalidator
pkgver=0.32.0
pkgrel=1
pkgdesc="Python library for validating X.509 certificates and paths"
arch=(any)
url="https://github.com/MatthiasValvekens/pyHanko/tree/master/pkgs/pyhanko-certvalidator"
license=(MIT)
depends=(python python-asn1crypto python-oscrypto python-cryptography python-uritools python-requests python-aiohttp)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-freezegun python-pytest-asyncio)
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha512sums=('c78d602532931f7d027e6291231633b48d0502b8b55af9fe6e2c35ca8048a51f9f2b63735750ec7a2eb2e4afbef416b7851ae6d586d7101f82e1531d6c619cf6')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
}

check(){
  cd $_name-$pkgver
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest -vv tests
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
