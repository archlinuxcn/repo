# Maintainer: Guillaume Hayot <ghayot@postblue.info>

pkgname=gnome-shell-extension-gsconnect
pkgver=66
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
b2sums=('f0eef3817c8d263ef258435da0a5e951a490d139be1e0d9172505d8fbb17fa350910cb71ac0ba15e36eb6f90c0073e584acb41a452c6adb3243d1c7329d79eba')
_uuid='gsconnect@andyholmes.github.io'

build() {
  arch-meson -Dinstalled_tests=false -Dfirewalld=true $pkgname-$pkgver build
  meson compile -C build
}

package() {
  DESTDIR="$pkgdir" meson install -C build
}
