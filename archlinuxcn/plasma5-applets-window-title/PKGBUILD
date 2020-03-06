# Maintainer: Alejandro Valdes <alejandrovaldes@live.com>

pkgname=plasma5-applets-window-title
pkgver=0.6.0
pkgrel=1
pkgdesc="Plasma 5 applet that shows the application title and icon for active window"
arch=(x86_64)
url="https://github.com/psifidotos/applet-window-title"
license=(GPL)
depends=(plasma-workspace)
source=("https://github.com/psifidotos/applet-window-title/archive/$pkgver.tar.gz")
sha512sums=('13ca0e92de0cf8fdd2f481d2580e540217efde30dad7cdc3d2c37364cb73bd488e41c15e839fdd5d16ea066b46d887dc29e7d40e7ec6271ca4e213e75b9c1448')

package() {
  _pkgdir="$pkgdir/usr/share/plasma/plasmoids/org.kde.windowtitle"
  mkdir -p "$_pkgdir"
  cp -r applet-window-title-$pkgver/* "$_pkgdir"
  rm "$_pkgdir/README.md"
}
