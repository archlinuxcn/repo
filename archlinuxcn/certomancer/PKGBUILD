# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=certomancer
pkgver=0.15.1
pkgrel=1
pkgdesc="Quickly construct, mock & deploy PKI test configurations using simple declarative configuration."
arch=(any)
url="https://github.com/MatthiasValvekens/$pkgname"
license=(MIT)
depends=(python python-aiohttp python-asn1crypto python-click python-pyyaml python-dateutil python-tzlocal python-cryptography python-requests-mock python-jinja python-werkzeug python-python-pkcs11)
makedepends=(git python-build python-installer python-setuptools python-setuptools-scm python-wheel)
checkdepends=(python-pytest python-pytz python-requests python-freezegun python-pytest-asyncio python-pyhanko-certvalidator)
source=(git+$url.git#tag=v$pkgver)
sha512sums=('6aa38e50ced7e3b901161f76728772f445b6cc31f2a2a69087a4c33778d58a0e7632424a0e804a4db84179d1b91345a1a2d0c8a15f151fe7bf808cd89fc80e17')

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
