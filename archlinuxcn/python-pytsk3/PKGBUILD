# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=pytsk3
pkgname=python-${_name}
pkgver=20260418
pkgrel=1
pkgdesc="Python bindings for The Sleuth Kit (libtsk)"
arch=(x86_64)
url="https://github.com/py4n6/pytsk"
license=(Apache-2.0)
depends=(gcc-libs glibc python sleuthkit)
makedepends=(git python-build python-installer python-setuptools python-wheel)
# Upstream git source is incomplete
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha512sums=('440300ea95894e7afcecf670c18dba0054b8fec4c6e9dc69b0ecf210da8ba3b5853e87b29986d6ca8bf87047704fe891dc846af6435fd2491535f95e4a399962')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 README -t "$pkgdir/usr/share/doc/$pkgname"
}
