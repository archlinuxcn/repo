# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=pytsk3
pkgname=python-${_name}
pkgver=20250801
pkgrel=1
pkgdesc="Python bindings for The Sleuth Kit (libtsk)"
arch=(x86_64)
url="https://github.com/py4n6/pytsk"
license=(Apache-2.0)
depends=(gcc-libs glibc python sleuthkit)
makedepends=(git python-build python-installer python-setuptools python-wheel)
# Upstream git source is incomplete
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha512sums=('9efb454570e7075a38b187868f41d9f70ed29e869d73478ec299deacc43cba57109c06fcfc07e46b4759b2fd958598836e100b52217737e1673614339cedf007')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 README -t "$pkgdir/usr/share/doc/$pkgname"
}
