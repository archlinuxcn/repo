# Maintainer: Guillaume Hayot <ghayot@postblue.info>

pkgname=gnome-shell-extension-gsconnect
pkgver=62
pkgrel=1
epoch=2
pkgdesc="KDE Connect implementation with GNOME Shell integration"
arch=('any')
url="https://github.com/GSConnect/gnome-shell-extension-gsconnect"
license=('GPL-2.0-or-later OR MPL-2.0')
makedepends=('meson' 'ninja' 'eslint' 'appstream' 'flake8' 'python-black')
depends=('gnome-shell')
optdepends=(
  'evolution-data-server: Contacts integration (Evolution)'
  'libgdata: Contacts integration (GNOME Online Accounts)'
  'gsound: Themed sound effects'
  'python-nautilus: Nautilus integration'
)
source=(https://github.com/GSConnect/$pkgname/archive/v$pkgver.tar.gz)
b2sums=('e33fddd6b8cabb702fdae466be3e3e970c45a57faacf3bdccbc56a8d0a7f077cf0aafd977a9e8868c961c6b2228e38ae9ddc96cfe8315f39b62d90245e20f2ee')
_uuid='gsconnect@andyholmes.github.io'

build() {
  arch-meson -Dinstalled_tests=false -Dfirewalld=true $pkgname-$pkgver build
  meson compile -C build
}

package() {
  DESTDIR="$pkgdir" meson install -C build
}
