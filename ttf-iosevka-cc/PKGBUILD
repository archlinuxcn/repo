# Maintainer: Markus Weimar <mail@markusweimar.de>
pkgname=ttf-iosevka-cc
pkgver=2.0.1
pkgrel=1
pkgdesc='A slender monospace typeface. Shape: default'
arch=('any')
url='https://be5invis.github.io/Iosevka/'
license=('custom:OFL')
depends=('fontconfig' 'xorg-font-utils')
conflicts=('ttf-iosevka-pack')
source=("https://github.com/be5invis/Iosevka/releases/download/v${pkgver}/04-iosevka-cc-${pkgver}.zip"
        "https://raw.githubusercontent.com/be5invis/Iosevka/master/LICENSE.md")
sha256sums=('d9116e779ae38cbab6dd0d324008e6235bc50a91ee8b24e7eebc10b71830152d'
            'a7a0e1da98ab1bae99a1f246f45e51720e0cc13a53b4a5b0692f64991d2191af')

package() {
    install -d ${pkgdir}/usr/share/fonts/TTF/
    install -m644 ${srcdir}/ttf/*.ttf ${pkgdir}/usr/share/fonts/TTF/
    install -D -m644 ${srcdir}/LICENSE.md ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md
}
