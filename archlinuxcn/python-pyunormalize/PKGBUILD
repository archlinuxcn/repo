# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=pyunormalize
pkgname=python-${_name}
pkgver=17.0.0
pkgrel=1
pkgdesc="Unicode normalization forms (NFC, NFKC, NFD, NFKD). A library independent of the Python core Unicode database."
arch=(any)
url="https://github.com/mlodewijck/${_name}"
license=('MIT AND Unicode-3.0')
depends=(python)
makedepends=(python-build python-installer python-setuptools python-wheel)
# https://github.com/mlodewijck/pyunormalize/issues/7
source=(https://files.pythonhosted.org/packages/source/${_name::1}/${_name//-/_}/${_name//-/_}-$pkgver.tar.gz)
sha512sums=('ba06f4b18e315a4d57060d695529b63148f87714fd0f30c702cc62058282ad6c9125b58e3f413da2bc06762778ed47f250e8ae11ab04a221aafd87bfad1b4054')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 UNICODE-LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
