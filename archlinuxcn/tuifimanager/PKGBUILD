# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=tuifimanager
_name=TUIFIManager
pkgver=4.1.5
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
sha256sums=('09e40b0fb06b41ab322ed6e46a137936cb4267b12b20182baa4706baf7ac4eee')

build() {
  cd "$_name-v.$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_name-v.$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
