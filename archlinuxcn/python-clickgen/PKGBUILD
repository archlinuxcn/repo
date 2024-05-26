# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=python-clickgen
_name=${pkgname#python-}
pkgver=2.2.3
pkgrel=1
pkgdesc="X11 & Windows cursor building API"
arch=('any')
url="https://github.com/ful1e5/clickgen"
license=('MIT')
depends=(
  'python-attrs'
  'python-numpy'
  'python-pillow'
  'python-toml'
  'python-yaml'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-setuptools'
  'python-wheel'
)
source=("${_name}-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('dd8d412d94739fe7c6b04bf51184fe0d3c84a4497052b21d2d9b409ce8654d39')

build() {
  cd "${_name}-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_name}-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
