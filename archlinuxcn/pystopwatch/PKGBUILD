#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=pystopwatch
pkgver=2018
pkgrel=1
pkgdesc='A stopwatch written in Python with a clock and two countdown functions that can minimize to the tray.'
arch=(any)
license=(GPL)
url="https://xyne.archlinux.ca/projects/pystopwatch"
depends=(gtk2 librsvg pygtk python2)
source=(
  https://xyne.archlinux.ca/projects/pystopwatch/src/pystopwatch-2018.tar.xz
  https://xyne.archlinux.ca/projects/pystopwatch/src/pystopwatch-2018.tar.xz.sig
)
sha512sums=(
  e75d2e6f41c6eb5647ab65ee06798c4b374cb3ab1f16c148bbb42685d3da175ffa5dce6c1af2c0afd2e1599c800aae3c1b2954a4738e9e66a01ef63a2175c8c4
  ac54f7b042287f6658b97ece939900aa9bca7fd018642d1fa153e1422a4b4428a89fee1cd87121acfd2714ea9eed74d044417dbd12f27fb64b86da1d41365dbf
)
md5sums=(
  4c4f21522d101e73ca2cc7f718d136aa
  3a31791f26dbedb92b6fab5e408ef873
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  install -Dm755 "$srcdir/$pkgname-$pkgver/$pkgname" "$pkgdir/usr/bin/$pkgname"
  install -Dm644 "$srcdir/$pkgname-$pkgver/$pkgname.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm644 "$srcdir/$pkgname-$pkgver/man/$pkgname.1.gz" "$pkgdir/usr/share/man/man1/$pkgname.1.gz"
}


# vim: set ts=2 sw=2 et:
