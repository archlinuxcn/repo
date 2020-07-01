# Maintainer: Tyler Swagar <buttpickle69@shaw.ca>

pkgname=ttf-signika
_commit='d774fc0799fdeddbd8720616a6d2d791be29fafa'
pkgver=1.002
pkgrel=3
pkgdesc='Sans-serif typeface from Google by Anna Giedryś'
arch=('any')
url='https://fonts.google.com/specimen/Signika'
license=('custom:SIL Open Font License v1.1')
depends=('xorg-fonts-encodings')
conflicts=('ttf-google-fonts-opinionated-git' 'ttf-signika-family-ib')
source=("Signika-Bold-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/signika/Signika-Bold.ttf"
        "Signika-Light-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/signika/Signika-Light.ttf"
        "Signika-Regular-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/signika/Signika-Regular.ttf"
        "Signika-SemiBold-${pkgver}.ttf::https://github.com/google/fonts/raw/${_commit}/ofl/signika/Signika-SemiBold.ttf"
        "${pkgname}-${pkgver}-OFL.txt::https://github.com/google/fonts/raw/${_commit}/ofl/signika/OFL.txt")
sha256sums=('2c64c17725f9413432c29edc78d074fd7c4a59797c1d2a962fd4ea3fec1f5090'
            '9ce8ef63ec2ed396fd9ce4e31b6f798d0143746d46bf6f5bcebdd8477d7978e7'
            'cea6cddac67d6baa98edfe13bafdea2650244dee850db1f530916e9acac6d1d7'
            'c654b274f8d0dbc0eafb39e670371e2fa4bc3984c8e950a15d025efc59cc8d1a'
            '1ba345a91338581e5f8fccc3e37e447ddea5b99ec9caec1b76c7c39492387d2f')

package() {
  install -dm 755 "${pkgdir}/usr/share/fonts/TTF"
  install -m 644 Signika-Bold-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Signika-Bold.ttf"
  install -m 644 Signika-Light-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Signika-Light.ttf"
  install -m 644 Signika-Regular-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Signika-Regular.ttf"
  install -m 644 Signika-SemiBold-${pkgver}.ttf "${pkgdir}/usr/share/fonts/TTF/Signika-SemiBold.ttf"
  install -Dm644 ${pkgname}-${pkgver}-OFL.txt "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
