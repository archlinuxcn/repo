# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=pyunormalize
pkgname=python-${_name}
pkgver=18.0.0
pkgrel=1
pkgdesc="Unicode normalization forms (NFC, NFKC, NFD, NFKD). A library independent of the Python core Unicode database."
arch=(any)
url="https://github.com/mlodewijck/${_name}"
license=('MIT AND Unicode-3.0')
depends=(python)
makedepends=(python-build python-installer python-setuptools python-wheel)
# https://github.com/mlodewijck/pyunormalize/issues/7
source=(https://files.pythonhosted.org/packages/source/${_name::1}/${_name//-/_}/${_name//-/_}-$pkgver.tar.gz)
sha512sums=('27995382c0237b649ed25c273107cee26884125466c446f7a8e88c666901056ac23d887bfc4fdcd0b0265ce47d7f4dca88ccf994c719e40a79983dba7d000353')

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
