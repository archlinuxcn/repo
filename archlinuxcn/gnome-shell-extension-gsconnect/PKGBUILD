# Maintainer: Guillaume Hayot <ghayot@postblue.info>

pkgname=gnome-shell-extension-gsconnect
pkgver=54
pkgrel=1
epoch=2
pkgdesc="KDE Connect implementation with GNOME Shell integration"
arch=('any')
url="https://github.com/GSConnect/gnome-shell-extension-gsconnect"
license=('GPL')
makedepends=('meson' 'ninja' 'eslint' 'appstream' 'flake8' 'python-black')
depends=('gnome-shell')
optdepends=(
  'folks: Contacts integration (Evolution)'
  'libgdata: Contacts integration (GNOME Online Accounts)'
  'gsound: Themed sound effects'
  'python-nautilus: Nautilus integration'
)
source=(https://github.com/GSConnect/$pkgname/archive/v$pkgver.tar.gz)
b2sums=('7d666775fc1ddf3ca76f59d2047b85cbc35f9953883941d1bca93f8711dcbf7ed5b8be697c300c13edf2195ffab10aa8f7edc7cbc6fde3d09797155f47349706')
_uuid='gsconnect@andyholmes.github.io'

build() {
  arch-meson -Dinstalled_tests=false -Dfirewalld=true $pkgname-$pkgver build
  meson compile -C build
}

package() {
  DESTDIR="$pkgdir" meson install -C build
}
