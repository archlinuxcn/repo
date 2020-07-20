# Maintainer: Markus Weimar <mail@markusweimar.de>
pkgname=ttf-iosevka-term
pkgver=3.3.1
pkgrel=1
pkgdesc='Typeface family designed for coding, terminal use and technical documents.'
arch=('any')
url='https://typeof.net/Iosevka/'
license=('OFL')
source=("https://github.com/be5invis/Iosevka/releases/download/v${pkgver}/ttf-iosevka-term-${pkgver}.zip"
        "${pkgname}-${pkgver}-${pkgrel}-LICENSE.md::https://raw.githubusercontent.com/be5invis/Iosevka/v${pkgver}/LICENSE.md")
sha256sums=('94d902b9aa008ded74dd8fa85e9203261950cc7100741b9be28a341ea0a68623'
            'e61c0988bb231a321f14cce1b119a468f279ea86826c32e943ab16dbf08c1ba9')

package() {
    install -d ${pkgdir}/usr/share/fonts/TTF/
    install -m644 ttf/*.ttf ${pkgdir}/usr/share/fonts/TTF/
    install -D -m644 ${pkgname}-${pkgver}-${pkgrel}-LICENSE.md ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md
}
