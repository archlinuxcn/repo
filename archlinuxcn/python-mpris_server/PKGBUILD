# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=python-mpris_server
_name=${pkgname#python-}
pkgver=0.9.0
pkgrel=1
epoch=1
pkgdesc="Integrate MPRIS Media Player support into your app"
arch=('any')
url="https://github.com/alexdelorenzo/mpris_server"
license=('AGPL-3.0-or-later')
depends=(
  'python-emoji'
  'python-gobject'
  'python-pydbus'
  'python-strenum'
  'python-unidecode'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-setuptools'
  'python-wheel'
)
source=("$_name-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('d259badafd2b63fa5f22e7993689f55907eb5f4e1394a699109507f77bec330f')

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
