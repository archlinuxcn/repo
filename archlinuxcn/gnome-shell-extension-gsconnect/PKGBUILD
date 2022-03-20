# Maintainer: Guillaume Hayot <ghayot@postblue.info>

pkgname=gnome-shell-extension-gsconnect
pkgver=53
pkgrel=1
pkgdesc="KDE Connect implementation with GNOME Shell integration"
arch=('any')
url="https://github.com/GSConnect/gnome-shell-extension-gsconnect"
license=('GPL')
makedepends=('meson' 'ninja' 'eslint' 'appstream')
depends=('gnome-shell')
optdepends=(
  'folks: Contacts integration (Evolution)'
  'libgdata: Contacts integration (GNOME Online Accounts)'
  'gsound: Themed sound effects'
  'python-nautilus: Nautilus integration'
)
source=(https://github.com/GSConnect/$pkgname/archive/v$pkgver.tar.gz)
sha256sums=('45f0c78e4d8842b9d062d092f4e1bb6db90df23c784869fd34202b3dbb4e6b27')
_uuid='gsconnect@andyholmes.github.io'

build() {
  arch-meson -Dinstalled_tests=false -Dfirewalld=true -Dpost_install=true -Dgsettings_schemadir="/usr/share/gnome-shell/extensions/$_uuid/schemas" $pkgname-$pkgver build
  meson compile -C build
}

package() {
  DESTDIR="$pkgdir" meson install -C build
  install -Dm644 "$pkgdir/usr/share/gnome-shell/extensions/$_uuid/schemas/org.gnome.Shell.Extensions.GSConnect.gschema.xml" -t \
    "$pkgdir/usr/share/glib-2.0/schemas"
}
