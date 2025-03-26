# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=pyhanko
pkgname=python-${_name}
pkgver=0.26.0
pkgrel=1
pkgdesc="sign and stamp PDF files"
arch=(any)
url="https://github.com/MatthiasValvekens/${_name}"
license=(MIT)
depends=(python python-asn1crypto python-qrcode python-tzlocal python-pyhanko-certvalidator python-click python-requests python-pyyaml python-cryptography python-uharfbuzz python-python-pkcs11 python-pillow python-barcode python-aiohttp python-oscrypto python-fonttools python-xsdata python-defusedxml python-dateutil)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-requests-mock certomancer python-freezegun python-pytest-asyncio python-defusedxml python-certomancer-csc-dummy python-pytest-aiohttp)
source=(${_name}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('fb154d3f5ae4aba42a08b6646445dca9c3b73be7edbe00dc4192baf34c1d1d7f79cfb975af59e75a5ea8e23e431c7610243339afb663c3a548918c9a76600029')

build() {
  cd pyHanko-$pkgver
  python -m build --wheel --no-isolation
}

check(){
  cd pyHanko-$pkgver
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest -vv pyhanko_tests
}

package() {
  cd pyHanko-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
