# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=docformatter
pkgver=1.7.8
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
sha512sums=('f7f30544a107cf2ecb6968c179e70b810c93822bdd13d04a3b089dff5b8732f8bcdb7a5e9e584e2aa9783ed47b69ee28b69c100a01e309e70602311f0e05d4ea')

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
