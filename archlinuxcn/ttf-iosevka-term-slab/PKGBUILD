# Maintainer: Markus Weimar <mail@markusweimar.de>
pkgname=ttf-iosevka-term-slab
pkgver=3.7.0
pkgrel=1
pkgdesc='Typeface family designed for coding, terminal use and technical documents.'
arch=('any')
url='https://typeof.net/Iosevka/'
license=('OFL')
source=("https://github.com/be5invis/Iosevka/releases/download/v${pkgver}/ttf-iosevka-term-slab-${pkgver}.zip"
        "${pkgname}-${pkgver}-${pkgrel}-LICENSE.md::https://raw.githubusercontent.com/be5invis/Iosevka/v${pkgver}/LICENSE.md")
sha256sums=('cb74ddf88bd08b449a163e691a884ccd45474f9d9af06bc5351e6968a57ef010'
            'e61c0988bb231a321f14cce1b119a468f279ea86826c32e943ab16dbf08c1ba9')

package() {
    install -d ${pkgdir}/usr/share/fonts/TTF/
    install -m644 ttf/*.ttf ${pkgdir}/usr/share/fonts/TTF/
    install -D -m644 ${pkgname}-${pkgver}-${pkgrel}-LICENSE.md ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md
}
