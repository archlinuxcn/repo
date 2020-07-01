# Maintainer: Tyler Swagar <buttpickle69@shaw.ca>

pkgname=ttf-oswald
_commit='dbb34644e36024fef3def6d268d30ead8f0ce113'
pkgver=4.101
pkgrel=2
pkgdesc='Sans-serif typeface from Google by Vernon Adams'
arch=('any')
url='https://fonts.google.com/specimen/Oswald'
license=('custom:SIL Open Font License v1.1')
depends=('xorg-fonts-encodings')
conflicts=('ttf-google-fonts-opinionated-git' 'otf-oswald-ib')
source=("Oswald-Bold-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/oswald/static/Oswald-Bold.ttf"
        "Oswald-ExtraLight-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/oswald/static/Oswald-ExtraLight.ttf"
        "Oswald-Light-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/oswald/static/Oswald-Light.ttf"
        "Oswald-Medium-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/oswald/static/Oswald-Medium.ttf"
        "Oswald-Regular-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/oswald/static/Oswald-Regular.ttf"
        "Oswald-SemiBold-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/oswald/static/Oswald-SemiBold.ttf"
        "${pkgname}-${pkgver}-OFL.txt::https://github.com/google/fonts/raw/${_commit}/ofl/oswald/OFL.txt")
sha256sums=('0cde70ba3b3398ab0bc19be74c7517442ef711846d33f286d7932fef9784e2d8'
            'f7e415a9685e50df9b4821a4c676089ed3cfea4037232f2ad4a994932bc9a24a'
            '292165793dab020fbe32fc3741d912b7fdc23e13c19c45451ea591f7ddfc7732'
            '8be76fb078487d3abe20d8d068d8ad8fc47bd25b504ac7b1e6642321feab149f'
            '43b55a174fb3f5a1e6218a5385f647d2eace04776ab58673f4a439381930006e'
            '4d6421e9e384ebca3db447336fc5e0e9f85e083ad4ca5e865c5f58a880808537'
            'ae05f8781a5ef38380ef3efe8cad86783610b6a780c6c278d7472f95310fccee')

package() {
  install -dm 755 "${pkgdir}/usr/share/fonts/TTF"
  install -m 644 Oswald-Bold-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Oswald-Bold.ttf"
  install -m 644 Oswald-ExtraLight-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Oswald-ExtraLight.ttf"
  install -m 644 Oswald-Light-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Oswald-Light.ttf"
  install -m 644 Oswald-Medium-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Oswald-Medium.ttf"
  install -m 644 Oswald-Regular-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Oswald-Regular.ttf"
  install -m 644 Oswald-SemiBold-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Oswald-SemiBold.ttf"
  install -Dm644 ${pkgname}-${pkgver}-OFL.txt "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
