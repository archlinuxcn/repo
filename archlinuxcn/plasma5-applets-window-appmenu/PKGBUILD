# Maintainer: Alejandro Valdes <alejandrovaldes@live.com>

pkgname=plasma5-applets-window-appmenu
pkgver=0.6.0
pkgrel=1
pkgdesc="Plasma 5 applet in order to show the window appmenu"
arch=(x86_64)
url="https://github.com/psifidotos/applet-window-appmenu"
license=(GPL)
depends=(qt5-base qt5-declarative plasma-workspace libxcb)
makedepends=(extra-cmake-modules plasma-framework kwindowsystem)
optdepends=(
  'libdbusmenu-gtk3: gtk3 appmenu support'
  'libdbusmenu-gtk2: gtk2 appmenu support'
)
source=($pkgname-$pkgver.tar.gz::"https://github.com/psifidotos/applet-window-appmenu/archive/v$pkgver.tar.gz")
sha256sums=('cc08e2a3d6c8a624064c5332f832e4fafdea541173ee8fcbd80ff410d8caac8e')

prepare() {
  mkdir -p build
}

build() {
  cd build
  cmake ../applet-window-appmenu-$pkgver \
    -DCMAKE_INSTALL_PREFIX=/usr
}

package() {
  cd build
  make DESTDIR="$pkgdir" install
}
