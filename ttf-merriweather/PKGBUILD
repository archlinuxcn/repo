# Maintainer: Tyler Swagar <buttpickle69@shaw.ca>

pkgname=ttf-merriweather
_commit='b848f42f0bc0a8bc53588c3688ca37890e1db0bd'
pkgver=2.002
pkgrel=1
epoch=1
pkgdesc='A typeface that is pleasant to read on screens by Sorkin Type Co'
arch=('any')
url='http://sorkintype.com/'
license=('custom:SIL Open Font License v1.1')
depends=('fontconfig' 'xorg-fonts-encodings' 'xorg-font-utils')
conflicts=('ttf-google-fonts-opinionated-git' 'ttf-merriweather-ib')
source=("Merriweather-Black-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/merriweather/Merriweather-Black.ttf"
        "Merriweather-BlackItalic-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/merriweather/Merriweather-BlackItalic.ttf"
        "Merriweather-Bold-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/merriweather/Merriweather-Bold.ttf"
        "Merriweather-BoldItalic-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/merriweather/Merriweather-BoldItalic.ttf"
        "Merriweather-Italic-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/merriweather/Merriweather-Italic.ttf"
        "Merriweather-Light-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/merriweather/Merriweather-Light.ttf"
        "Merriweather-LightItalic-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/merriweather/Merriweather-LightItalic.ttf"
        "Merriweather-Regular-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/merriweather/Merriweather-Regular.ttf"
        "${pkgname}-${pkgver}-OFL.txt::https://github.com/google/fonts/raw/${_commit}/ofl/merriweather/OFL.txt")
sha256sums=('dff1048499a2c245713dfa41e3683cfecfd15df757cc4cb20f85bceba7bfd58b'
            '42b5cdd80b293acb1d7a15958a2c2f8b6b95213709110777486763c75bc83ebf'
            '55139769a87085bff777f68e3ecf92450c21a04c5ddd1e9e9528960ba4088c9f'
            '403b1bece3d70420e65c670315693e9bca255e9c95884d9cb2b334838e67b509'
            'fc80dbac0ca9da894ae1801df9abe58f6dcca179ec4f8f6f7ea80fd13a1d387d'
            'd3ecc46bab128ed073ad9189bd7efdd2df455d8942ec056f14129bf35bcea7e5'
            '8521c8eb542adf178b19c7ab7a0210fb4715fe68bb6ea578be129277b642c1f0'
            'bc38fe756b3e259248183fc0b75ad81b02774f3ca68e5e544e925827b0186d40'
            'a7ba785ad99b6eae0444ab89910e512d4af9865937fddbcb5c72c4f59f55d6ad')

package() {
  install -dm 755 "${pkgdir}/usr/share/fonts/TTF"
  install -m 644 Merriweather-Black-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Merriweather-Black.ttf"
  install -m 644 Merriweather-BlackItalic-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Merriweather-BlackItalic.ttf"
  install -m 644 Merriweather-Bold-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Merriweather-Bold.ttf"
  install -m 644 Merriweather-BoldItalic-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Merriweather-BoldItalic.ttf"
  install -m 644 Merriweather-Italic-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Merriweather-Italic.ttf"
  install -m 644 Merriweather-Light-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Merriweather-Light.ttf"
  install -m 644 Merriweather-LightItalic-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Merriweather-LightItalic.ttf"
  install -m 644 Merriweather-Regular-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Merriweather-Regular.ttf"
  install -Dm644 ${pkgname}-${pkgver}-OFL.txt "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
