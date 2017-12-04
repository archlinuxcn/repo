# Maintainer: Gavin Lloyd <gavinhungry@gmail.com>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Hexchain Tong <i@hexchain.org>

pkgname=ttf-opensans
pkgver=1.101
pkgrel=1
pkgdesc='Sans-serif typeface commissioned by Google'
arch=('any')
url='https://fonts.google.com/specimen/Open+Sans'
license=('Apache')
depends=('fontconfig' 'xorg-fonts-encodings' 'xorg-font-utils')

_commit='beaec0837bd21524b57ecb435158f9011fc03999'
_raw="https://cdn.rawgit.com/google/fonts/${_commit}/apache/opensans"

source=("${_raw}/OpenSans-Bold.ttf"
        "${_raw}/OpenSans-BoldItalic.ttf"
        "${_raw}/OpenSans-ExtraBold.ttf"
        "${_raw}/OpenSans-ExtraBoldItalic.ttf"
        "${_raw}/OpenSans-Italic.ttf"
        "${_raw}/OpenSans-Light.ttf"
        "${_raw}/OpenSans-LightItalic.ttf"
        "${_raw}/OpenSans-Regular.ttf"
        "${_raw}/OpenSans-SemiBold.ttf"
        "${_raw}/OpenSans-SemiBoldItalic.ttf"
        "${_raw}condensed/OpenSansCondensed-Bold.ttf"
        "${_raw}condensed/OpenSansCondensed-Light.ttf"
        "${_raw}condensed/OpenSansCondensed-LightItalic.ttf")

sha256sums=('1b43de2449d39b65ff6f63315d4afda585f72fbbec2e3d9a56f59de6c75149d3'
            '3575d2afaaad69970380237a5d6357b6db241f53b77607482eaf9f299b8c07ec'
            '395f150240d43dff8baea6586baf5665337de57b8204a501fbd6148b2fe165b7'
            'd5de39bcdd010089d9db8dd1aebaefaf9e691bf9a49282ff43e1d1869b417892'
            '6cb918a707a06c4f98221d09344af4b98c9cb6184b13309a579caf0418d5eb74'
            '1c8d3cc6810ecd3623ebff7d2c3db1a44024260c5ae662f8166d69b9425828ed'
            'fda70df85987b394ff384b899703bc0e55ac7bdba94d06f47462e155cf0c0350'
            '13c03e22a633919beb2847c58c8285fb8a735ee97097d7c48fd403f8294b05f8'
            'b4c2050b25d3d296d5cf58589ca00816dc72df42262c2f629d5c6a984a161aa4'
            'a8f2af8e79f46686b1cfcfb3a1fd53e94e88308d7c6ee7f85c733f4796fcc3a0'
            '0c6bc4fecd8b88179d09508a12de72fa51d9a0b9842077c29c37ab586e7b6668'
            '8ae2a4d772519a12130bd844dab9916a575ac5ef8e371a643d6f67e15c7f8566'
            'aceec8387bad177ceb240bf628efe32c9b61f3c971d86a3cf00e4199142b81de')

package() {
  install -dm 755 "${pkgdir}/usr/share/fonts/TTF"
  install -m 644 *.ttf "${pkgdir}/usr/share/fonts/TTF/"
}
