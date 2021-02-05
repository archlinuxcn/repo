# Maintainer: Arnold G. <aurnoldg@gmail.com>

pkgname=ttf-comfortaa
pkgver=3.100
pkgrel=2
pkgdesc='Rounded geometric sans-serif typeface from Google by Johan Aakerlund'
arch=('any')
url='https://fonts.google.com/specimen/Comfortaa'
license=('custom:OFL')
conflicts=('ttf-google-fonts-git' 'ttf-google-fonts-opinionated-git')
source=("Comfortaa-Bold-${pkgver}.ttf::https://github.com/google/fonts/raw/4e6d978a7432514a9918b07863bb5280e7cc8815/ofl/comfortaa/Comfortaa-Bold.ttf"
        "Comfortaa-Light-${pkgver}.ttf::https://github.com/google/fonts/raw/4e6d978a7432514a9918b07863bb5280e7cc8815/ofl/comfortaa/Comfortaa-Light.ttf"
        "Comfortaa-Regular-${pkgver}.ttf::https://github.com/google/fonts/raw/4e6d978a7432514a9918b07863bb5280e7cc8815/ofl/comfortaa/Comfortaa-Regular.ttf"
        "${pkgname}-${pkgver}-OFL.txt::https://github.com/google/fonts/raw/4e6d978a7432514a9918b07863bb5280e7cc8815/ofl/comfortaa/OFL.txt")
sha256sums=('cc4756819298e823a066213a3ebc577a4a3e9e981fe66d25f00abbce84ca1675'
            'b92162d95548d8eef82928bc5c477def13dcdcfc1b37e3edfa4ec01957f1c9af'
            '96d580be232f31f051ec0573da14daf0490a0ff3e138cb616c443a14941c114f'
            '874ba013dd0547ea1d098cdc786297055333199d37ac1a6f8cef2577d2bc0531')

package() {
  install -dm 755 "${pkgdir}/usr/share/fonts/TTF"
  install -m 644 Comfortaa-Bold-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Comfortaa-Bold.ttf"
  install -m 644 Comfortaa-Light-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Comfortaa-Light.ttf"
  install -m 644 Comfortaa-Regular-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Comfortaa-Regular.ttf"
  install -Dm644 ${pkgname}-${pkgver}-OFL.txt "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
