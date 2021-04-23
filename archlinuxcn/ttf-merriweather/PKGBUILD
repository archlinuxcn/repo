# Maintainer: Tyler Swagar <buttpickle69@shaw.ca>

pkgname=ttf-merriweather
_commit='06e56b5a24d80a4a1ac94a71a0a05a98b5d02ef5'
pkgver=2.100
pkgrel=1
epoch=1
pkgdesc='A typeface that is pleasant to read on screens by Sorkin Type Co'
arch=('any')
url='http://sorkintype.com/'
license=('custom:SIL Open Font License v1.1')
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
sha256sums=('e4b178ebd76474428e59020635fafa11076f6a3b5e14cf41fac408bba75e75ae'
            'e302d95920cb4a161d4c81db6a24249fdc9ff30235b840780c4db49522149ad7'
            '8d2dcbd3041b5eab1739cb00cb58fadfea5c2c2977f410148d8432c471022879'
            '1d9bb02a953dc478f05bcc1ad8776809a8e7ce43f34ed53fb8224000a5163b08'
            '8969d6b6123e0b3b9e150c4411ac697ab941be075df38680229e2bd685b5691b'
            '32221799ab71877aeef75fa1615364408088e4d2fbd29e65caa97bfd92ff9594'
            '4780495ff32c2b547677e1e5946bdc62d44554137197af9fc196aa42584566cd'
            'a74a8658a74b5da43ddf32e211f4ad96bc0efc7d5cb921f78d3376aa2b8be5fe'
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
