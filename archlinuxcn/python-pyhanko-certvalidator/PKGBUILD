# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=pyhanko_certvalidator
pkgname=python-pyhanko-certvalidator
pkgver=0.31.4
pkgrel=1
pkgdesc="Python library for validating X.509 certificates and paths"
arch=(any)
url="https://github.com/MatthiasValvekens/pyHanko/tree/master/pkgs/pyhanko-certvalidator"
license=(MIT)
depends=(python python-asn1crypto python-oscrypto python-cryptography python-uritools python-requests python-aiohttp)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-freezegun python-pytest-asyncio)
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha512sums=('d87dc687b83ac320db2852db494e79e998f06cf94ec5b2da269f4964bacc9d9ba579a67d2bde94892f1e71e8d6547ee18fea295dccb030c820bc2a597190e74c')

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
