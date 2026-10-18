# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=pyhanko_certvalidator
pkgname=python-pyhanko-certvalidator
pkgver=0.33.0
pkgrel=1
pkgdesc="Python library for validating X.509 certificates and paths"
arch=(any)
url="https://github.com/MatthiasValvekens/pyHanko/tree/master/pkgs/pyhanko-certvalidator"
license=(MIT)
depends=(python python-asn1crypto python-oscrypto python-cryptography python-uritools python-requests python-aiohttp)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-freezegun python-pytest-asyncio)
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha512sums=('420f87fd13fe87084253cc24f29d33a95320f247ec447eef855d49193adc64cf5eeaea8ab3e4d4d5773c06e49abb100d595bf17fe4b15db7b221a4c90ebf0e16')

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
