#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=pystopwatch
pkgver=2012.12.24.1
pkgrel=3
pkgdesc='A stopwatch written in Python with a clock and two countdown functions that can minimize to the tray.'
arch=(any)
license=(GPL)
url="http://xyne.archlinux.ca/projects/pystopwatch"
depends=(python2 pygtk gtk2 librsvg)
source=(
  http://xyne.archlinux.ca/projects/pystopwatch/src/pystopwatch-2012.12.24.1.tar.xz
  http://xyne.archlinux.ca/projects/pystopwatch/src/pystopwatch-2012.12.24.1.tar.xz.sig
)
sha512sums=(
  4b3af373356eaafd14caeecb34150fef8e7099120855230dce7c0eabba68f75d497c3cc2eb733a086a02a96ae5feeca1898ba201a5f6f5597dcd32de9c80b3df
  b0cea3a92adc6ddb59eeba9a4da951848e564a76031bcfd23ad3ad93b1e2e38798e870dfc5e245078fb000da35b3706ded6b7e882ac025b53de85cb5410ded40
)
md5sums=(
  2bc39a6ac418bdf34cb96a22dc298e65
  48c6e896d5c0868744534e1b8445192c
)
install=pystopwatch.install
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  install -Dm755 "$srcdir/$pkgname-$pkgver/$pkgname" "$pkgdir/usr/bin/$pkgname"
  install -Dm644 "$srcdir/$pkgname-$pkgver/$pkgname.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm644 "$srcdir/$pkgname-$pkgver/man/$pkgname.1.gz" "$pkgdir/usr/share/man/man1/$pkgname.1.gz"
}


# vim: set ts=2 sw=2 et:
