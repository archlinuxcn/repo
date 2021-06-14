# Maintainer: Alejandro Valdes <alejandrovaldes@live.com>

pkgname=plasma5-applets-window-appmenu
pkgver=0.7.0
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
sha256sums=('318568d1176dba81eb1c89c03e8079fc8ba737cea64e9b1fa6abf1e2e33b5f6e')

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
