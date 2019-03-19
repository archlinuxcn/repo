# Maintainer: Guillaume Hayot <ghayot@postblue.info>

pkgname=gnome-shell-extension-gsconnect
pkgver=21
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
sha256sums=('228b7d3b41cd44d338784284a91f96f9f55ffb3f10c539c4907b1010871abcce')

package() {
  cd "$pkgname-$pkgver"
  meson build --prefix /usr --libdir lib/
  DESTDIR="${pkgdir}" ninja -C build install
}
