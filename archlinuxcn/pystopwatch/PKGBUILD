#Maintainer: Xyne <ac xunilhcra enyx, backwards>
pkgname=pystopwatch
pkgver=2019
pkgrel=1
pkgdesc='A stopwatch written in Python with a clock and two countdown functions that can minimize to the tray.'
arch=(any)
license=(GPL)
url="https://xyne.archlinux.ca/projects/pystopwatch"
depends=(gtk2 librsvg pygtk python2)
source=(
  https://xyne.archlinux.ca/projects/pystopwatch/src/pystopwatch-2019.tar.xz
  https://xyne.archlinux.ca/projects/pystopwatch/src/pystopwatch-2019.tar.xz.sig
)
sha512sums=(
  bfe88dd238c08b3b36f3789994e8cd30787e8cc1ee17bc8005828a2f5816b6d6c26b721899dcc5da8e867147bbc6acb5f3d86c623b6e9bd9ef23df2a41a1c52c
  6c25a08ef5b59de8c37a344f6cea16f741687544b60dff65f8181acf6d47b252c355ec39d79c97b413d0a271fcf68d387ef468c15d6efae339e194940b92af00
)
md5sums=(
  636cb26bcb89cd1344d9dbbed47a77fb
  750e12365a2bb0c58b15b90707fe688e
)
validpgpkeys=('EC3CBE7F607D11E663149E811D1F0DC78F173680')

package ()
{
  install -Dm755 "$srcdir/$pkgname-$pkgver/$pkgname" "$pkgdir/usr/bin/$pkgname"
  install -Dm644 "$srcdir/$pkgname-$pkgver/$pkgname.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm644 "$srcdir/$pkgname-$pkgver/man/$pkgname.1.gz" "$pkgdir/usr/share/man/man1/$pkgname.1.gz"
}


# vim: set ts=2 sw=2 et:
