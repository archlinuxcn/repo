# Maintainer: Håvard Pettersson <mail@haavard.me>
# Contributor: Kevin MacMartin <prurigro at gmail dot com>

_pkgname=qtox
pkgname=qtox-git
pkgver=r2712.2fed672
pkgrel=1
pkgdesc='Powerful Tox client written in C++/Qt that follows the Tox design guidelines.'
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h')
url='https://github.com/tux3/qTox'
license=('GPL3')
depends=(
  'desktop-file-utils'
  'libfilteraudio-git'
  'libxkbcommon-x11'
  'libxss'
  'opencv'
  'openal'
  'qt5-svg'
  'qrencode'
  'tox-git'
)
makedepends=('git' 'qt5-tools')
provides=("$_pkgname")
conflicts=("$_pkgname")
install=$pkgname.install
source=("$_pkgname::git+https://github.com/tux3/qTox.git")
sha512sums=('SKIP')

pkgver() {
  cd $_pkgname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd $_pkgname
  install -d build
  cd build
  qmake-qt5 ENABLE_SYSTRAY_UNITY_BACKEND=NO ..
  make
}

package() {
  # executable
  cd $_pkgname
  install -Dm755 build/$_pkgname "$pkgdir/usr/bin/$_pkgname"

  # xdg desktop file
  install -Dm644 qTox.desktop "$pkgdir/usr/share/applications/qTox.desktop"

  # icons
  cd img/icons
  for _icon in *.png; do
    _size=$(sed 's|^[^-]*-||;s|\.png||' <<< "$_icon")
    install -Dm644 "$_icon" "$pkgdir/usr/share/icons/hicolor/$_size/apps/$_pkgname.png"
  done
  install -Dm644 $_pkgname.svg "$pkgdir/usr/share/icons/hicolor/scalable/apps/$_pkgname.svg"
}
