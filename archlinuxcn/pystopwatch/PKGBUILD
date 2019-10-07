#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=pystopwatch
pkgver=2018.11
pkgrel=1
pkgdesc='A stopwatch written in Python with a clock and two countdown functions that can minimize to the tray.'
arch=(any)
license=(GPL)
url="https://xyne.archlinux.ca/projects/pystopwatch"
depends=(gtk2 librsvg pygtk python2)
source=(
  https://xyne.archlinux.ca/projects/pystopwatch/src/pystopwatch-2018.11.tar.xz
  https://xyne.archlinux.ca/projects/pystopwatch/src/pystopwatch-2018.11.tar.xz.sig
)
sha512sums=(
  bede0864e0bd24ec64425d63af46292b9e958737feccd7285c9b4af35bb0d7ffa75f72bbdb02202199c3c8c8ef9fd83884cdb4afe7e4f6bc35bbc676de4888e0
  3001edc9bbd6490648304cdf74e01d3ff6fdb37f86fd89f77b28259cf07299ba98cae8a4600ee9d6f439260270117fd8c87c14a65bb221fbb27c616425b40c43
)
md5sums=(
  8ab29745b15b5835efb1365a29891b82
  b10d77c45006862560d00eee190db7cf
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  install -Dm755 "$srcdir/$pkgname-$pkgver/$pkgname" "$pkgdir/usr/bin/$pkgname"
  install -Dm644 "$srcdir/$pkgname-$pkgver/$pkgname.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm644 "$srcdir/$pkgname-$pkgver/man/$pkgname.1.gz" "$pkgdir/usr/share/man/man1/$pkgname.1.gz"
}


# vim: set ts=2 sw=2 et:
