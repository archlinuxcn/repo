# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=certomancer
pkgver=0.12.3
pkgrel=2
pkgdesc="Quickly construct, mock & deploy PKI test configurations using simple declarative configuration."
arch=(any)
url="https://github.com/MatthiasValvekens/$pkgname"
license=(MIT)
depends=(python python-asn1crypto python-click python-pyyaml python-dateutil python-tzlocal python-cryptography python-requests-mock python-jinja python-werkzeug python-python-pkcs11)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-pytz python-requests python-freezegun python-pytest-asyncio python-pyhanko-certvalidator)
source=($pkgname-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('afd20c1ca8e106b63ae1e80716f04793ad659720cc478dc1a66883534e6cb0bc32ffc5a11d98ce3743e107e84225e512f98ce49d59efe3d722326796b1b76b46')

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
