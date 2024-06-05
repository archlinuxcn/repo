# Maintainer: Drommer <drommer@github.com>

_gitname="weather-widget-2"
pkgname=plasma6-applets-weather-widget-3-git
pkgver=r366.6f7ea94
pkgrel=1
pkgdesc="Weather Widget 3 for KDE Plasma 6"
arch=('x86_64')
url="https://github.com/blackadderkate/$_gitname"
license=('GPL-2.0-or-later')
depends=('plasma-workspace' 'qt6-5compat' 'qt6-declarative')
makedepends=('git' 'extra-cmake-modules')
source=("git+$url.git#branch=QT6")
sha256sums=('SKIP')
conflicts=('plasma5-applets-weather-widget' 'plasma-applets-weather-widget-2' 'plasma-applets-weather-widget-3')
provides=('plasma-applets-weather-widget-3')

pkgver() {
  cd "$_gitname"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  mkdir -p build
}

build() {
  cd build
  cmake ../$_gitname \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
}

package() {
  cd build
  make DESTDIR="$pkgdir" install
}
