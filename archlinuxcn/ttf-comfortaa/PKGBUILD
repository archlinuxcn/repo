# Maintainer: Arnold G. <aurnold at gmail dot com>

pkgname=ttf-comfortaa
pkgver=3.105
pkgrel=2
pkgdesc='Rounded geometric sans-serif typeface from Google by Johan Aakerlund'
arch=('any')
url='https://fonts.google.com/specimen/Comfortaa'
license=('custom:OFL')
conflicts=('ttf-google-fonts-git')
_commit='969f9e563003fd12e578354963917735113816b1'
source=("${pkgname}-${pkgver}.zip::https://fonts.google.com/download?family=Comfortaa")
source=(
  "Comfortaa-Bold-${pkgver}.ttf::https://github.com/googlefonts/comfortaa/raw/${_commit}/fonts/TTF/Comfortaa-Bold.ttf"
  "Comfortaa-Light-${pkgver}.ttf::https://github.com/googlefonts/comfortaa/raw/${_commit}/fonts/TTF/Comfortaa-Light.ttf"
  "Comfortaa-Medium-${pkgver}.ttf::https://github.com/googlefonts/comfortaa/raw/${_commit}/fonts/TTF/Comfortaa-Medium.ttf"
  "Comfortaa-Regular-${pkgver}.ttf::https://github.com/googlefonts/comfortaa/raw/${_commit}/fonts/TTF/Comfortaa-Regular.ttf"
  "Comfortaa-SemiBold-${pkgver}.ttf::https://github.com/googlefonts/comfortaa/raw/${_commit}/fonts/TTF/Comfortaa-SemiBold.ttf"
  "${pkgname}-${pkgver}-OFL.txt::https://github.com/googlefonts/comfortaa/raw/${_commit}/OFL.txt"
)
sha256sums=(
  '1960ed76ee4fe61de32b5779d104072d5d10431bf7fa45bc982d0cf71004843d'
  'ecdc9d45e17fd24b66def307d139efe48a317ebb6dc929b5e7f697423610d062'
  '8160917fc5d64ff6df33e9b568f048f6e1f3168fc525213eef1252e7fbff2f56'
  'f8e0843e8e373fd95beb1d8a10894c7413af437a77e5162fddbcbefdda45bb7d'
  '18cf25ac2e86f2e4edefb2f5f4d3d9b309629578a4c4c3196a2e556474d8e692'
  'bc85bae0b512b799bbfb2b916e4d0a34cfd963d09778cd783e248b479e67760a'
)

package() {
  install -dm 755 "${pkgdir}/usr/share/fonts/TTF"
  install -m 644 Comfortaa-Bold-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Comfortaa-Bold.ttf"
  install -m 644 Comfortaa-Light-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Comfortaa-Light.ttf"
  install -m 644 Comfortaa-Medium-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Comfortaa-Medium.ttf"
  install -m 644 Comfortaa-Regular-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Comfortaa-Regular.ttf"
  install -m 644 Comfortaa-SemiBold-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Comfortaa-SemiBold.ttf"
  install -Dm644 ${pkgname}-${pkgver}-OFL.txt "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
