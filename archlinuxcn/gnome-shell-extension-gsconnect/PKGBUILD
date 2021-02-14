# Maintainer: Guillaume Hayot <ghayot@postblue.info>

pkgname=gnome-shell-extension-gsconnect
pkgver=44
pkgrel=4
pkgdesc="KDE Connect implementation with GNOME Shell integration"
arch=('any')
url="https://github.com/andyholmes/gnome-shell-extension-gsconnect"
license=('GPL')
makedepends=('meson' 'ninja' 'eslint' 'appstream')
depends=('gnome-shell')
optdepends=(
  'folks: Contacts integration (Evolution)'
  'libgdata: Contacts integration (GNOME Online Accounts)'
  'gsound: Themed sound effects'
  'python-nautilus: Nautilus integration'
)
source=(https://github.com/andyholmes/$pkgname/archive/v$pkgver.tar.gz)
sha256sums=('ff0fc637df5352f74097caa2a1ba9d97ccb49a4834c49b3070a57fb6913a5f0d')
_uuid='gsconnect@andyholmes.github.io'

build() {
  arch-meson -Dinstalled_tests=false -Dfirewalld=true -Dpost_install=false -Dgsettings_schemadir="/usr/share/gnome-shell/extensions/$_uuid/schemas" $pkgname-$pkgver build
  meson compile -C build
}

package() {
  DESTDIR="$pkgdir" meson install -C build
  install -Dm644 "$pkgdir/usr/share/gnome-shell/extensions/$_uuid/schemas/org.gnome.Shell.Extensions.GSConnect.gschema.xml" -t \
    "$pkgdir/usr/share/glib-2.0/schemas"
}
