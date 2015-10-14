# Maintainer: Markus Tacker <m@cto.hiv>
# Contributor: Peter Hoeg <peter@hoeg.com>

_pkgver_major=2
_pkgver_minor=015
pkgname=ttf-hack
pkgver=${_pkgver_major}.${_pkgver_minor}
pkgrel=1
pkgdesc="Source Foundry Hack is is hand groomed and optically balanced typeface to be your go-to code face based on the Bitstream Vera Mono font."
arch=('any')
license=('SIL Open Font License 1.1 and Bitstream Vera License')
url="http://sourcefoundry.org/hack/"
depends=('fontconfig' 'xorg-fonts-encodings' 'xorg-font-utils')
install=$pkgname.install
source=("https://github.com/chrissimpkins/Hack/releases/download/v${pkgver}/Hack-v${_pkgver_major}_${_pkgver_minor}-ttf.zip")
sha256sums=('e59d11540fb63e225bd5441c420df302176ffb8f9cadae8c2ab4c5d8391f0c74')

package() {
  install -Dm644 -t $pkgdir/usr/share/fonts/TTF $srcdir/Hack-*.ttf
}
