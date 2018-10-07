# Maintainer: Markus Weimar <mail@markusweimar.de>
pkgname=ttf-iosevka-type-slab
pkgver=2.0.1
pkgrel=1
pkgdesc='A slender monospace typeface. Shape: default'
arch=('any')
url='https://be5invis.github.io/Iosevka/'
license=('custom:OFL')
depends=('fontconfig' 'xorg-font-utils')
conflicts=('ttf-iosevka-pack')
source=("https://github.com/be5invis/Iosevka/releases/download/v${pkgver}/07-iosevka-type-slab-${pkgver}.zip"
        "https://raw.githubusercontent.com/be5invis/Iosevka/master/LICENSE.md")
sha256sums=('7a3de564d9c8fb8099a0ef82899e1df0d299126a668e6873de3ba360920828a5'
            'a7a0e1da98ab1bae99a1f246f45e51720e0cc13a53b4a5b0692f64991d2191af')

package() {
    install -d ${pkgdir}/usr/share/fonts/TTF/
    install -m644 ${srcdir}/ttf/*.ttf ${pkgdir}/usr/share/fonts/TTF/
    install -D -m644 ${srcdir}/LICENSE.md ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md
}
