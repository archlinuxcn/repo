# Maintainer: Markus Weimar <mail@markusweimar.de>
pkgname=ttf-iosevka
pkgver=3.0.1
pkgrel=1
pkgdesc='Typeface family designed for coding, terminal use and technical documents.'
arch=('any')
url='https://typeof.net/Iosevka/'
license=('OFL')
source=("https://github.com/be5invis/Iosevka/releases/download/v${pkgver}/ttf-iosevka-${pkgver}.zip"
        "${pkgname}-${pkgver}-${pkgrel}-LICENSE.md::https://raw.githubusercontent.com/be5invis/Iosevka/v${pkgver}/LICENSE.md")
sha256sums=('22442302f90f57a174a6bbbb0c7971bc37a2e4a4f66c7cb7d11447aab7072fad'
            'e61c0988bb231a321f14cce1b119a468f279ea86826c32e943ab16dbf08c1ba9')

package() {
    install -d ${pkgdir}/usr/share/fonts/${pkgname}
    install -m644 ${srcdir}/ttf/*.ttf ${pkgdir}/usr/share/fonts/${pkgname}
    install -D -m644 ${pkgname}-${pkgver}-${pkgrel}-LICENSE.md ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md
}
