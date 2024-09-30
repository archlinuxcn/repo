# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=python-x-wr-timezone
_name=${pkgname#python-}
pkgver=1.0.1
pkgrel=1
pkgdesc="Handling of non-standard X-WR-TIMEZONE icalendar property in Python and Command Line"
arch=('any')
url="https://github.com/niccokunzmann/x-wr-timezone"
license=('LGPL-3.0-or-later')
depends=(
  'python-icalendar'
  'python-tzdata'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-setuptools'
  'python-wheel'
)
source=("$_name-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('ae6208da14289ae28a5eea837e12b06a7fc070b3903cdaa9149462666a119bca')

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
