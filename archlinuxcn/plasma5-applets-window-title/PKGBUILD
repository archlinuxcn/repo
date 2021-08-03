# Maintainer: Alejandro Valdes <alejandrovaldes@live.com>

pkgname=plasma5-applets-window-title
pkgver=0.7.0
pkgrel=2
pkgdesc="Plasma 5 applet that shows the application title and icon for active window"
arch=(any)
url="https://github.com/psifidotos/applet-window-title"
license=(GPL)
depends=(plasma-workspace)
source=("https://github.com/psifidotos/applet-window-title/archive/$pkgver.tar.gz")
sha512sums=('c08ac528ae9aae1d5745aa9aa13e1907b626c3290fa338961e89c3ee1ac94ad11303710561c50b39c77a40e2e76fb3269f43bdd814e367e085752ebf52e850b2')

package() {
  _pkgdir="$pkgdir/usr/share/plasma/plasmoids/org.kde.windowtitle"
  mkdir -p "$_pkgdir"
  cp -r applet-window-title-$pkgver/* "$_pkgdir"
  rm "$_pkgdir/README.md"
}
