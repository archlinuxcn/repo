# Maintainer: Tyler Swagar <buttpickle69@shaw.ca>

pkgname=ttf-merriweather
_commit='a792c77e48a672b821c0a4f98900ed39b6b0b3e9'
pkgver=2.003
pkgrel=1
epoch=1
pkgdesc='A typeface that is pleasant to read on screens by Sorkin Type Co'
arch=('any')
url='http://sorkintype.com/'
license=('custom:SIL Open Font License v1.1')
depends=('fontconfig' 'xorg-fonts-encodings' 'xorg-font-utils')
conflicts=('ttf-google-fonts-opinionated-git' 'ttf-merriweather-ib')
source=("Merriweather-Black-${pkgver}.ttf::https://github.com/EbenSorkin/Merriweather/raw/${_commit}/fonts/ttf/Merriweather-Black.ttf"
        "Merriweather-BlackItalic-${pkgver}.ttf::https://github.com/EbenSorkin/Merriweather/raw/${_commit}/fonts/ttf/Merriweather-BlackItalic.ttf"
        "Merriweather-Bold-${pkgver}.ttf::https://github.com/EbenSorkin/Merriweather/raw/${_commit}/fonts/ttf/Merriweather-Bold.ttf"
        "Merriweather-BoldItalic-${pkgver}.ttf::https://github.com/EbenSorkin/Merriweather/raw/${_commit}/fonts/ttf/Merriweather-BoldItalic.ttf"
        "Merriweather-Italic-${pkgver}.ttf::https://github.com/EbenSorkin/Merriweather/raw/${_commit}/fonts/ttf/Merriweather-Italic.ttf"
        "Merriweather-Light-${pkgver}.ttf::https://github.com/EbenSorkin/Merriweather/raw/${_commit}/fonts/ttf/Merriweather-Light.ttf"
        "Merriweather-LightItalic-${pkgver}.ttf::https://github.com/EbenSorkin/Merriweather/raw/${_commit}/fonts/ttf/Merriweather-LightItalic.ttf"
        "Merriweather-Regular-${pkgver}.ttf::https://github.com/EbenSorkin/Merriweather/raw/${_commit}/fonts/ttf/Merriweather-Regular.ttf"
        "${pkgname}-${pkgver}-OFL.txt::https://github.com/EbenSorkin/Merriweather/raw/${_commit}/OFL.txt")
sha256sums=('c62d90972158ee114b7dc10cc4496f2795087551a0c3ecba0a3653a5ab387be6'
            'd2dd7ddf29c1fa41a5d232ffa7c8fc76a0d5b31fd2c29c26f32e14fb1cbe743a'
            '60c5d1fb1ebc9b001a2768ef20ab6ee213386aea6e4a952479a57fd83d3d6eb3'
            '263492fbb7c1da5a9ff8a74796d34c0bfa91fa35f60ba186b46f8a56d8ba92c8'
            '4bf969bb2dddf44326a7dc152440d9130fcd5a5e2790c834268a2df46362a5b8'
            '8f1134ed77d1095bdaa804b1cf9adabe21a758060db3de0d29b5e32882eb374a'
            '94c743e850aafad18156e16885b63e03dd316e7ad33f61c1987c19991e6741d8'
            '6f3c50b5537925e499cbe79374d74290cb741f7ac2f15f3ddf25713473ff76cf'
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
