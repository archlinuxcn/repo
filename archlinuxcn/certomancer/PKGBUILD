# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=certomancer
pkgver=0.13.0
pkgrel=1
pkgdesc="Quickly construct, mock & deploy PKI test configurations using simple declarative configuration."
arch=(any)
url="https://github.com/MatthiasValvekens/$pkgname"
license=(MIT)
depends=(python python-asn1crypto python-click python-pyyaml python-dateutil python-tzlocal python-cryptography python-requests-mock python-jinja python-werkzeug python-python-pkcs11)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-pytz python-requests python-freezegun python-pytest-asyncio python-pyhanko-certvalidator)
source=($pkgname-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('1dbdd730753e4faad6d68093c1c412e49a70abd874aad33e314e2f10dae64d95e77ddbafbe9ac4f189deb7d4486738327241757a0ef4d3a79a7e31fb364e1b8b')

build() {
  cd $pkgname-$pkgver
  python -m build --wheel --no-isolation
}

check(){
  cd $pkgname-$pkgver
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest -vv tests
}

package() {
  cd $pkgname-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
  cp -r docs "$pkgdir/usr/share/doc/$pkgname"
}
