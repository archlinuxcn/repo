# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: Chris Lane <aur at chrislane dot com>
# Contributor: American_Jesus <american.jesus.pt AT gmail DOT com>
# Contributor: Federico Damián <federicodamians@gmail.com>
pkgname=vimix-icon-theme
_pkgver=2023-06-26
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A Material Design icon theme based on Paper Icon Theme"
arch=('any')
url="https://github.com/vinceliuice/vimix-icon-theme"
license=('CC BY-SA 4.0')
depends=('hicolor-icon-theme' 'gtk-update-icon-cache')
options=('!strip')
source=("$pkgname-$_pkgver.tar.gz::$url/archive/$_pkgver.tar.gz")
sha256sums=('40060c869ae040b9bbef21b39e0eea2e10201749478e6c4047aeeab04b0ee659')

prepare() {
   cd "$pkgname-$_pkgver"

  # Disable running gtk-update-icon-cache
  sed -i '/gtk-update-icon-cache/d' install.sh
}

package() {
  cd "$pkgname-$_pkgver"
  install -d "$pkgdir/usr/share/icons"
  ./install.sh -a -d "$pkgdir/usr/share/icons"

  install -Dm644 COPYING -t "$pkgdir/usr/share/licenses/$pkgname"
}
