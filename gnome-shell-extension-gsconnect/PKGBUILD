# Maintainer: Guillaume Hayot <ghayot@postblue.info>

pkgname=gnome-shell-extension-gsconnect
pkgver=14
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
sha256sums=('86dd959cda3dafc0c4f6d6c6e69b1a3acda8284c21a07dc1a73e42cda9b4a915')

package() {
  cd "$pkgname-$pkgver"
  meson build --prefix /usr --libdir lib/
  DESTDIR="${pkgdir}" ninja -C build install
}
