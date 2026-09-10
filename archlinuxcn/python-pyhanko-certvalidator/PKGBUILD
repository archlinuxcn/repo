# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=pyhanko_certvalidator
pkgname=python-pyhanko-certvalidator
pkgver=0.32.1
pkgrel=1
pkgdesc="Python library for validating X.509 certificates and paths"
arch=(any)
url="https://github.com/MatthiasValvekens/pyHanko/tree/master/pkgs/pyhanko-certvalidator"
license=(MIT)
depends=(python python-asn1crypto python-oscrypto python-cryptography python-uritools python-requests python-aiohttp)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-freezegun python-pytest-asyncio)
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha512sums=('0c4b89a1cacb96ee522164e9f129e9c2e9c72a91e84fd414a1b635668974b24b5f309250cda722860b0b32074a068f8bdc2cba51f765ad3686d84a935fd33dc7')

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
