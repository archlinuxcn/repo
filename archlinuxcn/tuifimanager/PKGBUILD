# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=tuifimanager
_name=TUIFIManager
pkgver=5.1.5
pkgrel=1
pkgdesc="A cross-platform terminal-based termux-oriented file manager"
arch=('any')
url="https://github.com/GiorgosXou/TUIFIManager"
license=('GPL-3.0-or-later')
depends=(
  'pyside6'
  'python'
  'python-requests'
  'python-send2trash'
  'python-uni-curses'
  'python-xlib'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-setuptools-scm'
  'python-wheel'
)
source=("$_name-$pkgver.tar.gz::$url/archive/refs/tags/v.$pkgver.tar.gz")
sha256sums=('5c162fcae89075a1e5bdbfa98be7cfc0e1eed686e0060730e8fd289cf95943ad')

build() {
  cd "$_name-v.$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_name-v.$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
