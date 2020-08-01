# Maintainer: Jiachen Yang <farseerfc@archlinux.org>
# Co-Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: poplarch <poplarch@gmail.com>

_pkgname=fcitx5-configtool
pkgbase=$_pkgname-git
pkgname=(fcitx5-configtool-git fcitx5-config-qt-git kbd-layout-viewer5-git)
pkgver=r310.7cc587d
pkgrel=1
pkgdesc="Config tools for Fcitx5, nightly build from git"
arch=('i686' 'x86_64')
url="https://github.com/fcitx/fcitx5-configtool"
license=('GPL')
depends=('fcitx5-qt5-git' 'kconfigwidgets' 'kitemviews' 'kirigami2' 'kpackage')
makedepends=('extra-cmake-modules' 'python' 'git' 'kcmutils')
conflicts=("$_pkgname")
provides=("$_pkgname")
source=("git+$url.git")
sha512sums=('SKIP')

pkgver() {
  cd $_pkgname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}



prepare() {
  mkdir build
}

build() {
  cd build

  cmake ../$_pkgname \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
  make
}

package_fcitx5-configtool-git() {
  conflicts=("$_pkgname")
  provides=("$_pkgname")
  replaces=("kcm-fcitx5-git")

  cd build
  make DESTDIR="$pkgdir" install
  mv "$pkgdir/usr/bin/fcitx5-config-qt" .
  mv "$pkgdir/usr/bin/kbd-layout-viewer5" .
  rmdir "$pkgdir/usr/bin/"
  mv "$pkgdir/usr/share/applications/kbd-layout-viewer5.desktop" .
  rmdir "$pkgdir/usr/share/applications/"
}

package_fcitx5-config-qt-git(){
  pkgdesc="Qt5 Config Module for Fcitx5"
  depends=('fcitx5-qt5-git' 'kitemviews' 'kwidgetsaddons')
  conflicts=("fcitx5-config-qt")
  provides=("fcitx5-config-qt")

  cd build
  install -Dm755 "fcitx5-config-qt" "$pkgdir/usr/bin/fcitx5-config-qt"
}

package_kbd-layout-viewer5-git(){
  pkgdesc="Keyboard layout viewer from Fcitx5"
  depends=('fcitx5-qt5-git')
  conflicts=("kbd-layout-viewer5")
  provides=("kbd-layout-viewer5")

  cd build
  install -Dm755 "kbd-layout-viewer5" "$pkgdir/usr/bin/kbd-layout-viewer5"
  install -Dm644 "kbd-layout-viewer5.desktop" "$pkgdir/usr/share/applications/kbd-layout-viewer5.desktop"
}
