# Maintainer: Rocket Aaron <i at rocka dot me>

pkgname=ttf-blobmoji
_tagname='15.1-beta1'
pkgver="${_tagname//-/}"
pkgrel=1
pkgdesc='Noto Emoji with extended Blob support'
arch=(any)
url='https://github.com/C1710/blobmoji'
license=('OFL-1.1')
provides=(emoji-font)
source=("https://github.com/C1710/blobmoji/releases/download/v${_tagname}/Blobmoji.ttf")
sha256sums=('61b588efe9960443a89de442feeab863744dea9dd169cba08c66762eb4d6952b')

package() {
  install -Dm644 Blobmoji.ttf "$pkgdir"/usr/share/fonts/TTF/Blobmoji.ttf
}
