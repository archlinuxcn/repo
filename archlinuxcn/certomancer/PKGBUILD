# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=certomancer
pkgver=0.15.0
pkgrel=2
pkgdesc="Quickly construct, mock & deploy PKI test configurations using simple declarative configuration."
arch=(any)
url="https://github.com/MatthiasValvekens/$pkgname"
license=(MIT)
depends=(python python-aiohttp python-asn1crypto python-click python-pyyaml python-dateutil python-tzlocal python-cryptography python-requests-mock python-jinja python-werkzeug python-python-pkcs11)
makedepends=(git python-build python-installer python-setuptools python-setuptools-scm python-wheel)
checkdepends=(python-pytest python-pytz python-requests python-freezegun python-pytest-asyncio python-pyhanko-certvalidator)
source=(git+$url.git#tag=v$pkgver)
sha512sums=('495ea58bb279e171d5816eb836bcd8233075d44b33409c7c110ab5c8177426b3389b1ae0302d606d2461920704ebfcfc71edd06f8b87b5561e9573ba1e71da23')

build() {
  cd $pkgname
  python -m build --wheel --no-isolation
}

check(){
  cd $pkgname
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest -vv tests
}

package() {
  cd $pkgname
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
  cp -r docs "$pkgdir/usr/share/doc/$pkgname"
}
