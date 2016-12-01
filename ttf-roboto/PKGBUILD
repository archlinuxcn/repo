# Maintainer: Michael Duell <michael.duell@rub.de> PGP-Fingerprint: FF8C D50E 66E9 5491 F30C  B75E F32C 939C 5566 FF77
# Co-Maintainer: Matt Hamilton <m@tthamilton.com>

pkgname=ttf-roboto
pkgver=131072
pkgrel=1
epoch=5
pkgdesc="Google's Android 5 system font."
arch=('any')
license=('Apache')
url="https://www.google.com/fonts/specimen/Roboto"
depends=('fontconfig' 'xorg-fonts-encodings' 'xorg-font-utils')
install=$pkgname.install
source=('https://raw.githubusercontent.com/google/fonts/master/apache/roboto/LICENSE.txt'
        'https://raw.githubusercontent.com/google/fonts/master/apache/roboto/Roboto-Black.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/roboto/Roboto-BlackItalic.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/roboto/Roboto-Bold.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/roboto/Roboto-BoldItalic.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/roboto/Roboto-Italic.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/roboto/Roboto-Light.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/roboto/Roboto-LightItalic.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/roboto/Roboto-Medium.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/roboto/Roboto-MediumItalic.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/roboto/Roboto-Regular.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/roboto/Roboto-Thin.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/roboto/Roboto-ThinItalic.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/robotocondensed/RobotoCondensed-Bold.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/robotocondensed/RobotoCondensed-BoldItalic.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/robotocondensed/RobotoCondensed-Italic.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/robotocondensed/RobotoCondensed-Light.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/robotocondensed/RobotoCondensed-LightItalic.ttf'
        'https://raw.githubusercontent.com/google/fonts/master/apache/robotocondensed/RobotoCondensed-Regular.ttf')

sha256sums=('cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30'
            '8ff04c6e5b13ebba574539918813c46d0fec170849a47e68c1d72aae469fa5ff'
            '9be6d400da270f2c104d40539f3f30338e21ee7bcc1012953706551c10415686'
            'ef2ab0e402d5cb9de893e263a2c44e57f57fec3974b0d981bfe84dec3dae83a1'
            '3157773ff81c4eb0883936e27054c05ed342beeef83a430a1d998213822d3da1'
            '044d2e3e3a17da487da46fc38cbd0a729deb9af044e563f66f8cdbc57421277e'
            'e7ea653ddec2d2a74d0dcbff099c009cc7469ec323a50c89a2915ce44ca4c0b4'
            '57577a8ab5086295d1026b1d53972fa0a2f7d1770a286d38be62bad4c7cdfbcd'
            '8559132c89ad51d8a2ba5b171887a44a7ba93776e205f553573de228e64b45f8'
            '91a1c11660929e8cfb726d7924a51b4042c0e77ec4c5b90b92fe5e45d26de759'
            'f0e5a21bf5c95e4c1bce2be98a3656ebcc6d42a21f41c4e3ebf69dd815702e54'
            '3b7a6691d978e81adfc92913cdfae58973151985b072df2a1b119ea937ba917e'
            '52079e4f67635c5a9bfc65873ceb6d75c773b25ab4ebdcb423f6e70aa036fd99'
            '0312269650316e083b0c6d006daef09fbb56b6d172e5c65c31e23f1c25dcd28c'
            '1b2a325a9956c169299a7fc805a0b9a224edec355d1d8bedf2fa3d0d4a190b29'
            'f546219826f3eb9f3d690ecbe4f1d559e6329b9ccca3e34e9bf440d327827bf5'
            '3c8dc0ab1183367c5628994f0896958a9f42fd58f4d4d2c3b0e63ffa3beaebe1'
            '8ce0c7eec44d511412b883db3edeed2df5002ea7611a89efa6c03fba5baa65bb'
            'd5cbe10cfb954e6d580525bd05536b21447ce29ab8a84e21da8a58b588190326'
)

pkgver() {
  fc-query Roboto-Bold.ttf | grep 'fontversion' | grep -o '[0-9]*'
}

package() {
  cd ${srcdir}
  install -d ${pkgdir}/usr/share/fonts/TTF/
  install -m644 *.ttf ${pkgdir}/usr/share/fonts/TTF/
  install -D -m644 LICENSE.txt ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
}

