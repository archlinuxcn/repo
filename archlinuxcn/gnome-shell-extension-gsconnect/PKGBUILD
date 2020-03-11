# Maintainer: Guillaume Hayot <ghayot@postblue.info>

pkgname=gnome-shell-extension-gsconnect
pkgver=34
pkgrel=1
pkgdesc="KDE Connect implementation with GNOME Shell integration"
arch=('any')
url="https://github.com/andyholmes/gnome-shell-extension-gsconnect"
license=('GPL')
makedepends=('meson' 'ninja' 'eslint')
depends=('gnome-shell')
optdepends=(
  'folks: Contacts integration (Evolution)'
  'libgdata: Contacts integration (GNOME Online Accounts)'
  'gsound: Themed sound effects'
  'python-nautilus: Nautilus integration'
)
source=(https://github.com/andyholmes/$pkgname/archive/v$pkgver.tar.gz)
sha256sums=('3155170a34e438c42a64e0604c295741ac67cc1c1040bb2967e5dd803d790cc3')

package() {
  cd "$pkgname-$pkgver"
  meson build --prefix /usr --libdir lib/
  DESTDIR="${pkgdir}" ninja -C build install
}
