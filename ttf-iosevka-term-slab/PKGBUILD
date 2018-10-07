# Maintainer: Markus Weimar <mail@markusweimar.de>
pkgname=ttf-iosevka-term-slab
pkgver=2.0.1
pkgrel=1
pkgdesc='A slender monospace typeface. Shape: default'
arch=('any')
url='https://be5invis.github.io/Iosevka/'
license=('custom:OFL')
depends=('fontconfig' 'xorg-font-utils')
conflicts=('ttf-iosevka-pack')
source=("https://github.com/be5invis/Iosevka/releases/download/v${pkgver}/06-iosevka-term-slab-${pkgver}.zip"
        "https://raw.githubusercontent.com/be5invis/Iosevka/master/LICENSE.md")
sha256sums=('7f70e51e2238d776d23fd549e7386cd9e1101c9a0ee738dc12b8128b910b0349'
            'a7a0e1da98ab1bae99a1f246f45e51720e0cc13a53b4a5b0692f64991d2191af')

package() {
    install -d ${pkgdir}/usr/share/fonts/TTF/
    install -m644 ${srcdir}/ttf/*.ttf ${pkgdir}/usr/share/fonts/TTF/
    install -D -m644 ${srcdir}/LICENSE.md ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md
}
