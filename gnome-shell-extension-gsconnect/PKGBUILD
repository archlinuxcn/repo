# Maintainer: Guillaume Hayot <ghayot@postblue.info>

pkgname=gnome-shell-extension-gsconnect
pkgver=15
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
  'python2-nautilus: Nautilus integration'
  'gsound: Themed sound effects'
)
source=(https://github.com/andyholmes/$pkgname/archive/v$pkgver.tar.gz)
sha256sums=('d2ea8e1ab16e1a9a06b8c82c1a312e35329cae455b2b8d98b3515e323ce228e5')

package() {
  cd "$pkgname-$pkgver"
  meson build --prefix /usr --libdir lib/
  DESTDIR="${pkgdir}" ninja -C build install
}
