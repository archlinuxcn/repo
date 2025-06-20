# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=certomancer-csc-dummy
pkgname=python-${_name}
pkgver=0.4.1
pkgrel=1
pkgdesc="A Certomancer-based demo CSC server for integration tests"
arch=(any)
url="https://github.com/MatthiasValvekens/${_name}"
license=(MIT)
depends=(python python-asn1crypto python-cryptography certomancer python-aiohttp python-pae)
makedepends=(python-build python-installer python-setuptools python-wheel)
source=(${_name}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('b1cb976debb2ad063c18a45e961235fa0a24a1f1f26e26e296326ec1c106656e1bd4557e677bf8b4023277f5906a33f51b5eb83207cde72916d7c2f445b31b55')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
