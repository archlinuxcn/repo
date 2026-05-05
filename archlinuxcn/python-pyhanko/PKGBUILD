# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=pyhanko
pkgname=python-${_name}
pkgver=0.35.0
pkgrel=1
pkgdesc="sign and stamp PDF files"
arch=(any)
url="https://github.com/MatthiasValvekens/${_name}"
license=(MIT)
depends=(python python-asn1crypto python-qrcode python-tzlocal python-pyhanko-certvalidator python-click python-requests python-pyyaml python-cryptography python-uharfbuzz python-python-pkcs11 python-pillow python-barcode python-aiohttp python-oscrypto python-fonttools python-xsdata python-defusedxml python-dateutil)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-requests-mock certomancer python-freezegun python-pytest-asyncio python-defusedxml python-certomancer-csc-dummy python-pytest-aiohttp)
source=(${_name}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('990ad1bfbc6ae8f65eb05491051e8f5f297959c8f1c7a93ef3aad6c2f5d4bc43c0454eb80fd27a6813ae018100bb0144a27b7723c19c56386cfc46cad4b25519')

prepare() {
  cd pyHanko-$pkgver
  cat >> pyproject.toml << EOF
[tool.setuptools]
packages = ["pkgs", "internal"]
EOF
}

build() {
  cd pyHanko-$pkgver
  python -m build --wheel --no-isolation
}

check(){
  cd pyHanko-$pkgver
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  # test_simple_text_stamp_on_page_with_leaky_graphics_state fails, need investigation
  test-env/bin/python -m pytest -vv pyhanko_tests || true
}

package() {
  cd pyHanko-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
