# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=python-pae
pkgver=0.1.0
pkgrel=1
pkgdesc="Pre-authentication encoding (PAE) implementation in Python"
arch=(any)
url="https://github.com/MatthiasValvekens/$pkgname"
license=(MIT)
depends=(python)
makedepends=(python-build python-installer python-poetry-core python-wheel python-sphinx python-sphinx_rtd_theme)
checkdepends=(python-pytest)
source=($pkgname-$pkgver.tar.gz::${url}/archive/$pkgver.tar.gz)
sha512sums=('3267aa72edc71b6bd3d76c09783bd99b23d98ac2099e1dae4ac469d233fed105b04717b42ca69adb9bb2013eeebebf7fd4aa013a25d5e1bc81891f0919473f6e')

build() {
  cd $pkgname-$pkgver
  python -m build --wheel --no-isolation
  make -C docs man
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
  install -Dm644 docs/_build/man/*.1 -t "$pkgdir/usr/share/man/man1"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.rst -t "$pkgdir/usr/share/doc/$pkgname"
}
