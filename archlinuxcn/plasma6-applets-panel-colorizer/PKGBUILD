# Maintainer: Luis Bocanegra <luisbocanegra17b at gmail dot com>
_gitname=plasma-panel-colorizer
pkgname=plasma6-applets-panel-colorizer
pkgver=4.3.0
pkgrel=1
pkgdesc="Latte-Dock and WM status bar customization features for the default Plasma panels"
arch=('any')
url="https://github.com/luisbocanegra/$_gitname"
license=('GPL3')
depends=('plasma-workspace' 'python' 'python-dbus')
makedepends=('extra-cmake-modules' 'gettext')
optdepends=('spectacle: take preset preview support')
source=("${_gitname}-${pkgver}.tar.gz::$url/archive/v${pkgver}/${_gitname}-${pkgver}.tar.gz")
sha256sums=('dff78dae1093fedf400148096e024437ba34b4cbd184932f33c39bfed37b701f')

build() {
  cd "${srcdir}/${_gitname}-$pkgver" || exit
  python ./kpac i18n --no-merge
  cmake -B build -S . -DINSTALL_PLASMOID=ON -DBUILD_PLUGIN=ON
  cmake --build build
}

package() {
  cd "${srcdir}/${_gitname}-$pkgver" || exit
  DESTDIR="$pkgdir" cmake --install build
  chmod 755 "$pkgdir/usr/share/plasma/plasmoids/luisbocanegra.panel.colorizer/contents/ui/tools/list_presets.sh"
  chmod 755 "$pkgdir/usr/share/plasma/plasmoids/luisbocanegra.panel.colorizer/contents/ui/tools/gdbus_get_signal.sh"
}
