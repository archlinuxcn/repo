# Maintainer: Guillaume Hayot <ghayot@postblue.info>

pkgname=gnome-shell-extension-gsconnect
pkgver=17
pkgrel=1
pkgdesc="KDE Connect implementation with GNOME Shell integration"
arch=('any')
url="https://github.com/andyholmes/gnome-shell-extension-gsconnect"
license=('GPL')
makedepends=('meson' 'ninja')
depends=('gnome-shell')
optdepends=(
  'sshfs: Browse remote files'
  'folks: Contacts integration (Evolution)'
  'libgdata: Contacts integration (GNOME Online Accounts)'
  'gsound: Themed sound effects'
  'python-nautilus: Nautilus integration'
)
source=(https://github.com/andyholmes/$pkgname/archive/v$pkgver.tar.gz)
sha256sums=('4d08a1306b254a62250c081541ec86479c3b9808f8392c171b2e62781703c47e')

package() {
  cd "$pkgname-$pkgver"
  meson build --prefix /usr --libdir lib/
  DESTDIR="${pkgdir}" ninja -C build install
}
