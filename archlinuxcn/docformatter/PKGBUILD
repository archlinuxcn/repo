# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=docformatter
pkgver=1.7.7
pkgrel=2
pkgdesc="Formats docstrings to follow PEP 257"
arch=(any)
url="https://github.com/PyCQA/$pkgname"
license=(MIT)
depends=(python python-charset-normalizer python-untokenize python-tomli)
makedepends=(python-build python-installer python-poetry-core python-wheel python-sphinx)
checkdepends=(python-pytest python-mock)
provides=(python-docformatter)
source=($pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz)
sha512sums=('0863846e5b226eb93a2e23b351328aead9ba5dd8ee578d2d1f0529c7c934a26b46086a47f5edf0efe359dd2f21c76d0f6a8ed2064048c103f537d183a667064a')

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
