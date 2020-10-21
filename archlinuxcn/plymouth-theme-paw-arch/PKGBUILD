# Maintainer: Ricardo Vieria <ricardo.vieira@ist.utl.pt>
pkgname='plymouth-theme-paw-arch'
pkgver=1
pkgrel=2
pkgdesc='Plymouth theme inspired by Mac OS X boot splash, but with Arch Linux logo'
arch=('any')
url='http://kahlil88.deviantart.com/art/Paw-Arch-Plymouth-Theme-208418769'
license=('unknown')
depends=('plymouth')
source=('http://fc05.deviantart.net/fs71/f/2011/131/6/7/paw_arch_plymouth_theme_by_kahlil88-d3g34y9.zip')
md5sums=('96725fabe237d1afaca2ae55ea80b367')

package() {
  cd "$srcdir/paw-arch"
  mkdir -p "$pkgdir/usr/share/plymouth/themes/paw-arch"
  install -Dm644 * "$pkgdir/usr/share/plymouth/themes/paw-arch"
}

# vim:set ts=2 sw=2 et:
