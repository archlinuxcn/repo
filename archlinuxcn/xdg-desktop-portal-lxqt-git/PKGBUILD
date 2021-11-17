# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>
# Modified from extra/xdg-desktop-portal-kde; original contributors:
# Contributor: Antonio Rojas <arojas@archlinux.org>

_pkgname=xdg-desktop-portal-lxqt
pkgname=$_pkgname-git
pkgver=0.0.0.r4.51b69e3
pkgrel=2
pkgdesc='A backend implementation for xdg-desktop-portal using Qt/KF5'
arch=(x86_64)
url='https://github.com/lxqt/xdg-desktop-portal-lxqt'
license=(LGPL)
depends=(qt5-base kwindowsystem xdg-desktop-portal lxqt-qtplugin-git libfm-qt-git)
makedepends=(cmake git)
provides=(xdg-desktop-portal-impl)
source=(git+$url)
sha256sums=('SKIP')

pkgver() {
  cd "$srcdir/$_pkgname"
  printf "0.0.0.r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cmake -B build -S $_pkgname \
    -DCMAKE_INSTALL_LIBEXECDIR=lib \
    -DCMAKE_INSTALL_PREFIX=/usr
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
