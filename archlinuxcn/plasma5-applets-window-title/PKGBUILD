# Maintainer: Alejandro Valdes <alejandrovaldes@live.com>

pkgname=plasma5-applets-window-title
pkgver=0.7.1
pkgrel=2
pkgdesc="Plasma 5 applet that shows the application title and icon for active window"
arch=(any)
url="https://github.com/psifidotos/applet-window-title"
license=(GPL)
depends=(plasma-workspace)
source=("https://github.com/psifidotos/applet-window-title/archive/$pkgver.tar.gz")
sha512sums=('ef00dbbed30d6fd3ee872ddf211e12567943ecfa9cf1cbeb1b8e494b869fd8592d666d57cd09ef4fcd16c468c4ce48c42bdaccc88b3ede33c7e442d3e3f623b9')

package() {
  _pkgdir="$pkgdir/usr/share/plasma/plasmoids/org.kde.windowtitle"
  mkdir -p "$_pkgdir"
  cp -r applet-window-title-$pkgver/* "$_pkgdir"
  rm "$_pkgdir/README.md"
}
