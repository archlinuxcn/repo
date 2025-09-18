# Contributor: Michał Wojdyła < micwoj9292 at gmail dot com >
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Christopher Arndt <aur -at- chrisarndt -dot- de>
# Contributor: Gaute Hope <eg@gaute.vetsj.com>
# Contributor: Melissa Padilla <mpadilla2 at hotmail dot com>

pkgname=python-future
pkgver=1.0.0
pkgrel=4
pkgdesc="Clean single-source support for Python 3 and 2"
url="https://python-future.org/"
arch=('any')
license=('MIT')
depends=('python')
provides=('futurize' 'pasteurize')
checkdepends=('python-requests' 'python-pytest')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
optdepends=('python-setuptools: futurize and pasteurize scripts')
options=('!emptydirs')
source=("https://pypi.io/packages/source/f/future/future-$pkgver.tar.gz")
sha512sums=('8e28d53172e3ae7b3b27c424a48fb698a6e86bf1c648cdf74e7fd57d34901a9bda18429fe4e176d70be67fc6c80b7f961b3021356594e38b5f294406af40bc61')
install=future.install
build() {
  cd "$srcdir"/future-$pkgver
  python -m build --wheel
}
# https://github.com/PythonCharmers/python-future/issues/640
# https://python-future.org/overview.html#status
check() {
  cd "$srcdir"/future-$pkgver
  # test_future needs python2 so it is disabled here
  #PYTHONPATH="$PWD/build/lib:$PYTHONPATH" pytest -v tests/test_future
  PYTHONPATH="$PWD/build/lib:$PYTHONPATH" pytest -v tests/test_past
}

package() {
  cd future-$pkgver

  python -m installer --destdir="$pkgdir" dist/*.whl
  install -D -m644 LICENSE.txt \
    "$pkgdir"/usr/share/licenses/$pkgname/LICENSE.txt
}
