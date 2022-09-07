# Maintainer: Arnold G. <aurnold at gmail dot com>

pkgname=ttf-comfortaa
pkgver=3.101
pkgrel=1
pkgdesc='Rounded geometric sans-serif typeface from Google by Johan Aakerlund'
arch=('any')
url='https://fonts.google.com/specimen/Comfortaa'
license=('custom:OFL')
conflicts=('ttf-google-fonts-git')
source=("Comfortaa-Bold-${pkgver}.ttf::https://github.com/googlefonts/comfortaa/raw/${pkgver}/fonts/TTF/Comfortaa-Bold.ttf"
        "Comfortaa-Light-${pkgver}.ttf::https://github.com/googlefonts/comfortaa/raw/${pkgver}/fonts/TTF/Comfortaa-Light.ttf"
        "Comfortaa-Regular-${pkgver}.ttf::https://github.com/googlefonts/comfortaa/raw/${pkgver}/fonts/TTF/Comfortaa-Regular.ttf"
        "${pkgname}-${pkgver}-OFL.txt::https://raw.githubusercontent.com/googlefonts/comfortaa/${pkgver}/OFL.txt")
sha256sums=('32ff43f8112ececd38a15b4b7a9273ddb6a133d711e1df2e6280a881f76f06e2'
            'bec64af51957b6b25c6cc9edcf5fe4480fbde825a46b367a9a3189317275dda1'
            '096bf9e1ebb88fa17406dd1a2829d39e2ab2834058277655d9ee332e743a66c7'
            'bc85bae0b512b799bbfb2b916e4d0a34cfd963d09778cd783e248b479e67760a')

package() {
  install -dm 755 "${pkgdir}/usr/share/fonts/TTF"
  install -m 644 Comfortaa-Bold-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Comfortaa-Bold.ttf"
  install -m 644 Comfortaa-Light-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Comfortaa-Light.ttf"
  install -m 644 Comfortaa-Regular-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Comfortaa-Regular.ttf"
  install -Dm644 ${pkgname}-${pkgver}-OFL.txt "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
