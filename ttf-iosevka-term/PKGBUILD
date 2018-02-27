# Maintainer: Markus Weimar <mail@markusweimar.de>
pkgname=ttf-iosevka-term
pkgver=1.14.1
pkgrel=1
pkgdesc='A slender monospace typeface. Shape: default.'
arch=('any')
url='https://be5invis.github.io/Iosevka/'
license=('custom:OFL')
depends=('fontconfig' 'xorg-font-utils')
conflicts=('ttf-iosevka-pack'
           'ttf-iosevka-term-ss01'
           'ttf-iosevka-term-ss02'
           'ttf-iosevka-term-ss03'
           'ttf-iosevka-term-ss04'
           'ttf-iosevka-term-ss05'
           'ttf-iosevka-term-ss06'
           'ttf-iosevka-term-ss07'
           'ttf-iosevka-term-ss08'
           'ttf-iosevka-term-ss09'
           'ttf-iosevka-term-ss10'
           'ttf-iosevka-term-ss11')
source=("https://github.com/be5invis/Iosevka/releases/download/v${pkgver}/02-iosevka-term-${pkgver}.zip"
        "https://raw.githubusercontent.com/be5invis/Iosevka/master/LICENSE.md")
sha256sums=('bcff19eeec85ff5e9b38464916357aebc2f3441eccb69c72ee57936358c21ced'
            'a7a0e1da98ab1bae99a1f246f45e51720e0cc13a53b4a5b0692f64991d2191af')

package() {
    install -d ${pkgdir}/usr/share/fonts/TTF/
    install -m644 ${srcdir}/ttf/*.ttf ${pkgdir}/usr/share/fonts/TTF/
    install -D -m644 ${srcdir}/LICENSE.md ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md
}
