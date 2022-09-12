# Maintainer: Arnold G. <aurnold at gmail dot com>

pkgname=ttf-comfortaa
pkgver=3.105
pkgrel=1
pkgdesc='Rounded geometric sans-serif typeface from Google by Johan Aakerlund'
arch=('any')
url='https://fonts.google.com/specimen/Comfortaa'
license=('custom:OFL')
conflicts=('ttf-google-fonts-git')
source=("${pkgname}-${pkgver}.zip::https://fonts.google.com/download?family=Comfortaa")
sha256sums=('SKIP')

package() {
  install -dm 755 "${pkgdir}/usr/share/fonts/TTF"
  install -m 644 static/*.ttf "${pkgdir}/usr/share/fonts/TTF/"
  install -Dm644 OFL.txt "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
