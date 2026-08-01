# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=parsimonious
pkgname=python-${_name}
pkgver=0.11.0
pkgrel=2
pkgdesc="The fastest pure-Python PEG parser I can muster"
arch=(any)
url="https://github.com/erikrose/${_name}"
license=(MIT)
depends=(python python-regex)
makedepends=(python-build python-installer python-setuptools python-setuptools-scm python-wheel)
checkdepends=(python-pytest)
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha512sums=('4d4e54ba74f205c937771db4ccc93ecd2831fa030a767ec1af010d9f3905e1ad0620e0f0d07b2711bec6276f4f921c9851c31f6f29ef93490b0e765891d63239')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
}

check(){
  cd $_name-$pkgver
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest -vv parsimonious/tests/
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.rst -t "$pkgdir/usr/share/doc/$pkgname"
}
