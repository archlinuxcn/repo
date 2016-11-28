# Maintainer: Colin Keenan <colinnkeenan at gmail dot com>

pkgname=silentcast
pkgver=2.4
pkgrel=1
pkgdesc="Silent Screencast: video record your screen and make it into an animated gif"
arch=('any')
url="https://github.com/colinkeenan/silentcast"
license=('GPL')
depends=('bash' 'ffmpeg' 'imagemagick' 'xdotool' 'xorg-xrandr' 'xorg-xwininfo' 'wmctrl' 'python-gobject' 'python-cairo' 'xdg-utils' 'yad')
optdepends=('libappindicator-gtk2: necessary when running KDE Plasma 5 desktop to enable the right-click->done option from the systray icon')
install=${pkgname}.install

source=($url"/archive/v"$pkgver".tar.gz")
md5sums=('f3be42817fa07f33df14bd7177c87511')

package() {
  cd "$pkgname-$pkgver"
  install -D -m755 silentcast "$pkgdir/usr/bin/silentcast"
  install -m755 genffcom "$pkgdir/usr/bin"
  install -m755 temptoanim "$pkgdir/usr/bin"
  install -D -m755 silentcast.conf "$pkgdir/etc/silentcast.conf"
  install -D -m755 transparent_window.py "$pkgdir/usr/share/silentcast/transparent_window.py"
  install -m755 unity_indicator.py "$pkgdir/usr/share/silentcast"
  install -m644 stop?.png "$pkgdir/usr/share/silentcast"
  install -D -m644 silentcast.png "$pkgdir/usr/share/pixmaps/silentcast.png"
  install -D -m644 silentcast.desktop "$pkgdir/usr/share/applications/silentcast.desktop"
  install -D -m644 README.md "$pkgdir/usr/share/doc/silentcast/README.md"
  install -m644 *png "$pkgdir/usr/share/doc/silentcast"
  install -m644 *gif "$pkgdir/usr/share/doc/silentcast"
  install -D -m755 manpages/silentcast.1 "$pkgdir/usr/share/man/man1/silentcast.1"
  install -m755 manpages/genffcom.1 "$pkgdir/usr/share/man/man1/"
  install -m755 manpages/temptoanim.1 "$pkgdir/usr/share/man/man1/"
}
