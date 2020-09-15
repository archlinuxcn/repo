# Maintainer: Alejandro Valdes <alejandrovaldes@live.com>

pkgname=plasma5-applets-window-appmenu
pkgver=0.6.0.r36.g57e999f
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
source=($pkgname-$pkgver.zip::"https://github.com/psifidotos/applet-window-appmenu/archive/57e999f01f8bbbb60de1f4fef9e73a6437bb4667.zip")
sha256sums=('4ac39c3c9575f104c5db9a55b271f24f97d42d54d86cb734740bd828a851c4fe')

prepare() {
  mkdir -p build
}

build() {
  cd build
  cmake ../applet-window-appmenu-57e999f01f8bbbb60de1f4fef9e73a6437bb4667 \
    -DCMAKE_INSTALL_PREFIX=/usr
}

package() {
  cd build
  make DESTDIR="$pkgdir" install
}
