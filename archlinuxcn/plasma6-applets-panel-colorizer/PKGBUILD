# Maintainer: Luis Bocanegra <luisbocanegra17b at gmail dot com>
_gitname=plasma-panel-colorizer
pkgname=plasma6-applets-panel-colorizer
pkgver=8.2.0
pkgrel=1
pkgdesc="Latte-Dock and WM status bar customization features for the KDE Plasma panels"
arch=('any')
url="https://github.com/luisbocanegra/plasma-panel-colorizer"
license=('GPL-3.0-or-later')
depends=('libplasma' 'python' 'python-dbus')
makedepends=('gcc' 'extra-cmake-modules' 'gettext' 'layer-shell-qt')
optdepends=('spectacle: take preset preview support')
source=("${_gitname}-${pkgver}.tar.gz::$url/archive/v${pkgver}/${_gitname}-${pkgver}.tar.gz")
sha256sums=('3756148efa227caa86126ec67f6a70bcc2fab97b94603ad37744dcc905e4e55e')

build() {
  cd "${srcdir}/${_gitname}-$pkgver"
  python ./kpac i18n --no-merge
  cmake -B build -S . -DINSTALL_PLASMOID=ON -DBUILD_PLUGIN=ON
  cmake --build build
}

package() {
  cd "${srcdir}/${_gitname}-$pkgver"
  DESTDIR="$pkgdir" cmake --install build
  chmod 755 "$pkgdir/usr/share/plasma/plasmoids/luisbocanegra.panel.colorizer/contents/ui/tools/list_presets.sh"
  chmod 755 "$pkgdir/usr/share/plasma/plasmoids/luisbocanegra.panel.colorizer/contents/ui/tools/gdbus_get_signal.sh"
}
