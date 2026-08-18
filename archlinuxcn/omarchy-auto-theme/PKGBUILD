# Maintainer: Jackey <jfdnet@users.noreply.github.com>

pkgname=omarchy-auto-theme
pkgver=1.0.0
pkgrel=1
pkgdesc="Auto-switch Omarchy light/dark theme by sunrise/sunset (NOAA solar algorithm)"
arch=('any')
url="https://github.com/jfdnet/omarchy-auto-theme"
license=('MIT')
depends=('python' 'omarchy')
optdepends=(
    'python-dbus: geoclue automatic location'
    'python-gobject: geoclue automatic location'
    'geoclue: geoclue automatic location'
)
source=("https://github.com/jfdnet/omarchy-auto-theme/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('d5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed')

package() {
    cd "$srcdir/omarchy-auto-theme-$pkgver"
    make DESTDIR="$pkgdir" PREFIX=/usr install
}
