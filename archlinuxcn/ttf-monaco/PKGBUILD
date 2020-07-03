# Maintainer: Kewl <xrjy@nygb.rh.bet(rot13)>
# Contributor: Dennis Fink <metalgamer@c3l.lu>
# Contributor: Tobias Frilling <tobias@frilling-online.de>

pkgname=ttf-monaco
pkgver=6.1
pkgrel=6
pkgdesc="The Monaco monospaced sans-serif typeface with special characters added"
arch=('any')
license=('unknown')
url="https://github.com/todylu/monaco.ttf"
source=(Monaco_Linux.ttf::"${url}/blob/master/monaco.ttf?raw=true")
sha256sums=('7c67ce805b52338822998eb309aee40b505863b9cb8776080668e2a4e5a99025')

package() {
    install -Dm644 Monaco_Linux.ttf -t "${pkgdir}/usr/share/fonts/TTF/"
}
