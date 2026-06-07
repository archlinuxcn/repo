# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=pyhanko_certvalidator
pkgname=python-pyhanko-certvalidator
pkgver=0.31.1
pkgrel=2
pkgdesc="Python library for validating X.509 certificates and paths"
arch=(any)
url="https://github.com/MatthiasValvekens/pyHanko/tree/master/pkgs/pyhanko-certvalidator"
license=(MIT)
depends=(python python-asn1crypto python-oscrypto python-cryptography python-uritools python-requests python-aiohttp)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-freezegun python-pytest-asyncio)
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha512sums=('be308d2f5f93119b9e369993ff2ad02fb9f1ab7fd41cb3866ac2ae0165e3216a73c3ad57b3867fb52fbb2d4489171672d94d0c3a8f278163fd82afec7c4cc9ba')

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
