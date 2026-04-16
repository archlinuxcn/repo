# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=pytsk3
pkgname=python-${_name}
pkgver=20260416
pkgrel=1
pkgdesc="Python bindings for The Sleuth Kit (libtsk)"
arch=(x86_64)
url="https://github.com/py4n6/pytsk"
license=(Apache-2.0)
depends=(gcc-libs glibc python sleuthkit)
makedepends=(git python-build python-installer python-setuptools python-wheel)
# Upstream git source is incomplete
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha512sums=('f3ae9cbb362a9a0fb83ed8f45bbc7989f4644fdb599e7be461fa5d0a4b7489a5ce2816de7ed639300f77eae9c6b13f7d2bb505efa79d50c9e391e6484bcc371e')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 README -t "$pkgdir/usr/share/doc/$pkgname"
}
