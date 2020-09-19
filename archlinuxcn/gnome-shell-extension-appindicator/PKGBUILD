pkgname=gnome-shell-extension-appindicator
pkgver=34
pkgrel=1
pkgdesc="Integrates AppIndicators into GNOME Shell"
arch=('any')
url="https://github.com/ubuntu/gnome-shell-extension-appindicator"
license=('GPL')
depends=('gnome-shell>=3.34')
optdepends=(
	'libappindicator-gtk2: support GTK+2 applications'
	'libappindicator-gtk3: support GTK+3 applications'
)
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('2d2721e3195a847ae184c9c354dd79062a6d22b6257225b952df7531e6661558')

package() {
	cd "$pkgname-$pkgver"

	local _uuid="appindicatorsupport@rgcjonas.gmail.com"
	local _destdir="$pkgdir/usr/share/gnome-shell/extensions/$_uuid"

	install -d "$_destdir"
	cp --parents -t "$_destdir" metadata.json *.js interfaces-xml/*.xml
}
