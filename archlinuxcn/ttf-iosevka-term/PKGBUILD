# Maintainer: Markus Weimar <mail@markusweimar.de>
pkgname=ttf-iosevka-term
pkgver=2.3.3
pkgrel=1
pkgdesc='A slender monospace typeface. Shape: default'
arch=('any')
url='https://be5invis.github.io/Iosevka/'
license=('custom:OFL')
depends=('fontconfig' 'xorg-font-utils')
conflicts=('ttf-iosevka-pack')
source=("https://github.com/be5invis/Iosevka/releases/download/v${pkgver}/02-iosevka-term-${pkgver}.zip"
        "${pkgname}-${pkgver}-${pkgrel}-LICENSE.md::https://raw.githubusercontent.com/be5invis/Iosevka/v${pkgver}/LICENSE.md")
sha256sums=('00fce617405fccd7fbf7316dadd3f6b3ccb1e276f2910e9a9cde12e3f058b4d7'
            'ecfd74a1d6749bf509cee122870da0186bccfae446e3f6bc5faff253577ab000')

package() {
    install -d ${pkgdir}/usr/share/fonts/${pkgname}
    install -m644 ${srcdir}/ttf/*.ttf ${pkgdir}/usr/share/fonts/${pkgname}
    install -D -m644 ${pkgname}-${pkgver}-${pkgrel}-LICENSE.md ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md
}
