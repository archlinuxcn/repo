# Maintainer: ouyangjun( oyj805557641@gmail.com)
# Maintainer: Markus Weimar <mail@markusweimar.de>
# Contributor: dongfengweixiao ( dongfengweixiao [at] hotmail [dot] com  )
pkgname=ttf-inziu-iosevka
pkgver=1.13.3
pkgrel=1
pkgdesc='A composite of Iosevka, M+ and Source Han Sans.'
arch=('any')
url='https://be5invis.github.io/Iosevka/inziu.html'
license=('custom:OFL')
depends=('fontconfig' 'xorg-font-utils')
source=("http://7xpdnl.dl1.z0.glb.clouddn.com/inziu-iosevka-${pkgver}.7z"
        "https://raw.githubusercontent.com/be5invis/Iosevka/master/LICENSE.md")
sha256sums=('de3b49f941552cd12c4fc5552e49325b040a2818fcbb850d227e49eb720253ed'
            'a7a0e1da98ab1bae99a1f246f45e51720e0cc13a53b4a5b0692f64991d2191af')

package() {
    install -d ${pkgdir}/usr/share/fonts/TTC/
    install -m644 ${srcdir}/*.ttc ${pkgdir}/usr/share/fonts/TTC/
    install -D -m644 ${srcdir}/LICENSE.md ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md
}
