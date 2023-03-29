# Maintainer: Filipe Nascimento <flipee at tuta dot io>

_pkgname=applet-latte-separator
pkgname=plasma5-applets-latte-separator
pkgver=0.1.2
pkgrel=1
pkgdesc="Plasma applet that acts as a separator between applets"
arch=('any')
url="https://github.com/psifidotos/$_pkgname"
license=('GPL')
depends=('plasma-workspace')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('0f6e2b63ee1f769d586e6a59376de02d1ba8615cd9999e8853dc4df21ded4ba0')

package() {
    cd "$srcdir/$_pkgname-$pkgver"
    _pkgdir="$pkgdir/usr/share/plasma/plasmoids/org.kde.latte.separator"

    install -Dm644 metadata.desktop -t "$_pkgdir"
    find contents/ -type f -exec install -Dm644 "{}" "$_pkgdir/{}" \;
}
