# Maintainer: hamki <hamki.do2000@gmail.com>
# Contributor: Luis Martinez <luis dot martinez at disroot dot org>

pkgname=nordic-theme
pkgver=2.1.0
pkgrel=1
pkgdesc="GTK theme using the Nord color palette"
arch=('any')
url="https://github.com/EliverLara/Nordic"
license=('GPL3')
source=("$pkgname-$pkgver.tar.xz::$url/releases/download/v$pkgver/Nordic.tar.xz")
sha256sums=('cce429254c31473571963b5125e8fb652ce517bbec5245b1e17fe975b9bfd10b')

package() {
	cd Nordic
	find assets cinnamon gnome-shell gtk-* metacity-1 xfwm4 index.theme \
		-type f -exec install -Dm 644 '{}' "$pkgdir/usr/share/themes/Nordic/{}" \;
}
