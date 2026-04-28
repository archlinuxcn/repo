# Maintainer: Luis Bocanegra <luisbocanegra17b at gmail dot com>
_gitname=plasma-panel-colorizer
pkgname=plasma6-applets-panel-colorizer
pkgver=7.0.1
pkgrel=1
pkgdesc="Latte-Dock and WM status bar customization features for the KDE Plasma panels"
arch=('any')
url="https://github.com/luisbocanegra/plasma-panel-colorizer"
license=('GPL-3.0-or-later')
depends=('libplasma' 'python' 'python-dbus')
makedepends=('gcc' 'extra-cmake-modules' 'gettext')
optdepends=('spectacle: take preset preview support')
source=("${_gitname}-${pkgver}.tar.gz::$url/archive/v${pkgver}/${_gitname}-${pkgver}.tar.gz")
sha256sums=('f80e7e71206c66d4bbe5be759d33dc76deea9475ce94c5f64c4b7e43f7d03192')

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
