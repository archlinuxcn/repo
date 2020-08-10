# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: Chris Lane <aur at chrislane dot com>
# Contributor: American_Jesus <american.jesus.pt AT gmail DOT com>
# Contributor: Federico Damián <federicodamians@gmail.com>
pkgname=vimix-icon-theme
_pkgver=2020-07-10
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A Material Design icon theme based on Paper Icon Theme"
arch=('any')
url="https://github.com/vinceliuice/vimix-icon-theme"
license=('CC BY-SA 4.0')
depends=('hicolor-icon-theme' 'gtk-update-icon-cache')
options=('!strip')
source=("$pkgname-$_pkgver.tar.gz::$url/archive/$_pkgver.tar.gz")
sha256sums=('08e69fbd9b7ae5fe68ddf5dea86407c87b446ac64ef037f05eb9aa4f27f4d06f')

package() {
	cd "$pkgname-$_pkgver"
	install -dm755 "$pkgdir/usr/share/icons"
	./install.sh -a -d "$pkgdir/usr/share/icons"

	install -Dm644 COPYING -t "$pkgdir/usr/share/licenses/$pkgname"
}
