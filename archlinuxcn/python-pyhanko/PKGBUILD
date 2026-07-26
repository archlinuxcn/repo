# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=pyhanko
pkgname=python-$_name
pkgver=0.36.1
pkgrel=2
pkgdesc="sign and stamp PDF files"
arch=(any)
url="https://github.com/MatthiasValvekens/$_name"
license=(MIT)
depends=(python python-asn1crypto python-qrcode python-tzlocal python-pyhanko-certvalidator python-requests python-pyyaml python-cryptography python-uharfbuzz python-python-pkcs11 python-pillow python-barcode python-aiohttp python-oscrypto python-fonttools python-xsdata python-defusedxml python-dateutil python-lxml python-signxml)
makedepends=(git python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-requests-mock certomancer python-freezegun python-pytest-asyncio python-defusedxml python-certomancer-csc-dummy python-pytest-aiohttp)
source=(git+$url.git#tag=v$pkgver)
sha256sums=('5b8775df319fe1d0dd826790fe9e3366603ab07f5ccf5f9cace2fcfd073f170b')

prepare() {
  cd $_name
  sed -i "s/^version = .*/version = \"$pkgver\"/" pkgs/$_name/pyproject.toml
  sed -i \
    -e "s/^__version__ = .*/__version__ = '$pkgver'/" \
    -e "s/^__version_info__ = .*/__version_info__ = (${pkgver//./, })/" \
    pkgs/$_name/src/pyhanko/version/__init__.py
}

build() {
  cd $_name/pkgs/$_name
  python -m build --wheel --no-isolation
}

check(){
  cd $_name/pkgs/$_name
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  PYTHONPATH="$srcdir/$_name/internal/common-test-utils/src" \
    test-env/bin/python -m pytest -vv tests
}

package() {
  cd $_name/pkgs/$_name
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
