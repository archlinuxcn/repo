# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=docformatter
pkgver=1.7.6
pkgrel=1
pkgdesc="Formats docstrings to follow PEP 257"
arch=(any)
url="https://github.com/PyCQA/$pkgname"
license=(MIT)
depends=(python python-charset-normalizer python-untokenize python-tomli)
makedepends=(python-build python-installer python-poetry-core python-wheel python-sphinx)
checkdepends=(python-pytest python-mock)
provides=(python-docformatter)
source=($pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz)
sha512sums=('26915cfa3d966e44b6d4b4ef73ad033fade6015dc5c3e2a6d1960c68700f1332bff2bff0480a4bfc948c5550422ade69d8c7ee7ec329c7f1a8127bf32a7cef86')

build() {
  cd $pkgname-$pkgver
  python -m build --wheel --no-isolation
  make -C docs man
}

check(){
  cd $pkgname-$pkgver
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  export VIRTUAL_ENV=$(realpath test-env)
  # https://github.com/PyCQA/docformatter/issues/274
  test-env/bin/python -m pytest -vv tests || true
}

package() {
  cd $pkgname-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 docs/build/man/$pkgname.1 -t "$pkgdir/usr/share/man/man1"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.rst -t "$pkgdir/usr/share/doc/$pkgname"
}
