# Maintainer: Guillaume Hayot <ghayot@postblue.info>

pkgname=gnome-shell-extension-gsconnect
pkgver=48
pkgrel=1
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
sha256sums=('3f90fbbb6885309279201a043d79028b76db0e552044ffa21b407f0cf9e0a0d9')
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
