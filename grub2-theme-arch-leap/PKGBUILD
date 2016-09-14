# Maintainer: Michael Straube <michael_straube web de>
pkgname=grub2-theme-arch-leap
pkgver=1
pkgrel=1
pkgdesc="Arch Linux branded theme adapted from openSUSE Leap 42.1"
url="https://github.com/mstraube/grub2-theme-arch-leap"
arch=('any')
license=('GPL')
depends=('grub')
source=("https://github.com/mstraube/$pkgname/archive/$pkgver.tar.gz")
sha1sums=('0fa3aaf3957aeba7adc3e838ae08179495fc969c')

package() {
  cd $pkgname-$pkgver/theme
  install -dm755 "$pkgdir/boot/grub/themes/arch-leap"
  install -m644 * "$pkgdir/boot/grub/themes/arch-leap/"
}
