# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=python-uni-curses
_name=unicurses
pkgver=3.0.0
pkgrel=1
pkgdesc="Unified Curses Wrapper for Python"
arch=('any')
url="https://github.com/unicurses/unicurses"
license=('GPL-3.0-or-later')
depends=('ncurses' 'python' 'python-x256')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
source=("$_name-$pkgver.tar.gz::$url/archive/refs/tags/v.$pkgver.tar.gz")
sha256sums=('a9d81ec28d0fb32fb5ccc1cd80dfa5c2ffd7bdcf28f70c62e7334b35253bcd48')

prepare() {
  cd "$_name-v.$pkgver"

  # Don't package Windows binaries
  sed -i '/package_data/d' setup.py
}

build() {
  cd "$_name-v.$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_name-v.$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
