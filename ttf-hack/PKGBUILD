# Maintainer: Markus Tacker <m@cto.hiv>
# Contributor: Peter Hoeg <peter@hoeg.com>

_pkgver_major=2
_pkgver_minor=018
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
sha256sums=('7dbafae9b1f6c5b0763b227e51c5485cc4ef6d9b0fec4914622ddb9fe235334c')

package() {
  install -Dm644 -t $pkgdir/usr/share/fonts/TTF $srcdir/Hack-*.ttf
}
