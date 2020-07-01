# Maintainer: Tyler Swagar <buttpickle69@shaw.ca>

pkgname=ttf-quintessential
_commit='883939708704a19a295e0652036369d22469e8dc'
pkgver=1.001
pkgrel=5
pkgdesc='Calligraphic typeface from Google by Brian J. Bonislawsky'
arch=('any')
url='https://fonts.google.com/specimen/Quintessential'
license=('custom:SIL Open Font License v1.1')
depends=('xorg-fonts-encodings')
conflicts=('ttf-google-fonts-opinionated-git' 'otf-quintessential-ib')
source=("Quintessential-Regular-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/quintessential/Quintessential-Regular.ttf"
        "${pkgname}-${pkgver}-OFL.txt::https://github.com/google/fonts/raw/${_commit}/ofl/quintessential/OFL.txt")
sha256sums=('73d192f10dbfc716214aae282afb93036f12415d16adc9d6d0e981f34d829d32'
            '0786594992757ea0290ae4a490ab9249728f372adb13959c0c8ae4fec83057ff')

package() {
  install -dm 755 "${pkgdir}/usr/share/fonts/TTF"
  install -m 644 Quintessential-Regular-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Quintessential-Regular.ttf"
  install -Dm644 ${pkgname}-${pkgver}-OFL.txt "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
