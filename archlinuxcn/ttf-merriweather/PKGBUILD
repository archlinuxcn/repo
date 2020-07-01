# Maintainer: Tyler Swagar <buttpickle69@shaw.ca>

pkgname=ttf-merriweather
_commit='ae0bf55e53517ac98cc74c375a383ad4c36f937a'
pkgver=2.005
pkgrel=2
epoch=1
pkgdesc='A typeface that is pleasant to read on screens by Sorkin Type Co'
arch=('any')
url='http://sorkintype.com/'
license=('custom:SIL Open Font License v1.1')
depends=('xorg-fonts-encodings')
conflicts=('ttf-google-fonts-opinionated-git' 'ttf-merriweather-ib')
source=("Merriweather-Black-${pkgver}.ttf::https://github.com/SorkinType/Merriweather/raw/${_commit}/fonts/ttfs/Merriweather-Black.ttf"
        "Merriweather-BlackItalic-${pkgver}.ttf::https://github.com/SorkinType/Merriweather/raw/${_commit}/fonts/ttfs/Merriweather-BlackItalic.ttf"
        "Merriweather-Bold-${pkgver}.ttf::https://github.com/SorkinType/Merriweather/raw/${_commit}/fonts/ttfs/Merriweather-Bold.ttf"
        "Merriweather-BoldItalic-${pkgver}.ttf::https://github.com/SorkinType/Merriweather/raw/${_commit}/fonts/ttfs/Merriweather-BoldItalic.ttf"
        "Merriweather-Italic-${pkgver}.ttf::https://github.com/SorkinType/Merriweather/raw/${_commit}/fonts/ttfs/Merriweather-Italic.ttf"
        "Merriweather-Light-${pkgver}.ttf::https://github.com/SorkinType/Merriweather/raw/${_commit}/fonts/ttfs/Merriweather-Light.ttf"
        "Merriweather-LightItalic-${pkgver}.ttf::https://github.com/SorkinType/Merriweather/raw/${_commit}/fonts/ttfs/Merriweather-LightItalic.ttf"
        "Merriweather-Regular-${pkgver}.ttf::https://github.com/SorkinType/Merriweather/raw/${_commit}/fonts/ttfs/Merriweather-Regular.ttf"
        "${pkgname}-${pkgver}-OFL.txt::https://github.com/SorkinType/Merriweather/raw/${_commit}/OFL.txt")
sha256sums=('73e4deb0e7c241a7e98ddcb9216c322be2a7f50df9b542f4aa3233154c12a852'
            '1f83c77a970d9832143f481b32ea705f97f238a0e7bb2c6ecd30a1de1b902f54'
            'a03a68750a3ef5c50833ba8313e7ee4a1907c811da1a6e96a2f64718850706f4'
            '96c3e940049b0f7fb500620998d5aa0ad0a901c6a67c359859dd90b88d20e373'
            'e9e7c00e9606290a2fc4e478f76256fe5e7b39f4e5c79bb3264595ffb18402bc'
            '5acd66e1d1841fc30649e195480a9552fa7e55d62c73b8b4795513761f911fb6'
            'ba900a4ad03e5ee0fe0d91c083a0711bb1f434074950535a24583ad9e0bbf83d'
            '22ce375fea4f4c394dafb0637b7c18fc1783c64524da6806159c771efbe9a47a'
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
