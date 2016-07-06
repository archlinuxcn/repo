# Maintainer: farseerfc <farseerfc@gmail.com>

_pkgname=aseman-qt-tools
pkgname=${_pkgname}-git
pkgver=1.0.0
pkgrel=1
pkgdesc="the shared tools and functions used in the aseman's projects"
arch=('x86_64' 'i686')
license=('GPL3')
url="https://launchpad.net/libqtelegram"
depends=('qt5-multimedia' 'qt5-location' 'qt5-declarative' 'qt5-quickcontrols' 'qt5-sensors' 'qtkeychain')
makedepends=('cmake' 'git')
source=("$_pkgname"::"git+https://github.com/Aseman-Land/aseman-qt-tools.git")
md5sums=('SKIP')
conflicts=('aseman-qt-tools')
provides=("aseman-qt-tools=${pkgver}")

pkgver() {
  cd "$srcdir/$_pkgname"
  ( set -o pipefail
    git describe --long --tags 2>/dev/null | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g' ||
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
  )
}

prepare() {
  cd $_pkgname
  mkdir -p build
}

build() {
  cd $_pkgname/build
  qmake-qt5 -r QMAKE_CFLAGS_ISYSTEM= QT+=widgets QT+=multimedia QT+=dbus QT+=sensors QT+=positioning  ../asemantools.pro
  make
}

package() {
  cd $_pkgname/build
  make INSTALL_ROOT="$pkgdir" install
}
