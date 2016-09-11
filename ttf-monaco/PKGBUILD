# Maintainer: Dennis Fink <metalgamer@c3l.lu>
# Maintainer: Tobias Frilling <tobias@frilling-online.de>

pkgname=ttf-monaco
pkgver=6.1
pkgrel=3
pkgdesc="A monospaced sans-serif typeface by Apple Inc."
arch=('any')
license=('unknown')
url="http://www.apple.com/"
depends=('fontconfig')
replaces=('monaco_linux' 'monaco-linux-font')
conflicts=('monaco_linux' 'monaco-linux-font')
install=ttf-monaco.install
source=("Monaco_Linux.ttf::https://github.com/todylu/monaco.ttf/blob/master/monaco.ttf?raw=true")
sha1sums=('da768f1a6aac6b10aa5c92f2415a5e6b215ee9ff')

package() {
  install -d "$pkgdir/usr/share/fonts/TTF/"
  install -m644 Monaco_Linux.ttf "$pkgdir/usr/share/fonts/TTF/"
}
