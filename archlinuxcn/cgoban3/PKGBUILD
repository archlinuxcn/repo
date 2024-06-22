# Maintainer: TH Campbell (dysphoria) <thcampbell (at) protonmail (dot) com>
# Contributor: Jonathan Schaeffer <Joschaeffer@gmail.com>

pkgname=cgoban3
pkgver=3.5.144
pkgrel=3
pkgdesc='A KGS client and SGF editor'
url='https://www.gokgs.com/'
arch=('any')
license=('Freeware')
depends=('desktop-file-utils' 'java-runtime' 'bash')
source=(
        'https://files.gokgs.com/javaBin/cgoban.jar'
        'cgoban3'
        'cgoban3.png'
        'cgoban3.desktop'
       )
sha256sums=('7a137f690536dd912d0e1ffeaf71f63c33c1ad6860a0c7e011f2aae6ad3c9056'
            'e1ba41f3a461f1a67818f25518a53106c30add18e9b37ca2558ae05fbf67e362'
            'a87ecc7d285cf19ab176a437dfb22ab8841eff2f64348cc432557d879347d510'
            '62348a1f2a4559159d2262409d948e4eb514f5b244d069fc78fa44383ae5a025')
noextract=('cgoban.jar')

package() {
        cd ${srcdir}
        install -D -m644 cgoban.jar  "${pkgdir}/usr/share/java/cgoban3/cgoban.jar"
        install -D -m644 cgoban3.desktop "${pkgdir}/usr/share/applications/cgoban3.desktop"
        install -D -m644 cgoban3.png "${pkgdir}/usr/share/pixmaps/cgoban3.png"
        install -D -m755 cgoban3 "${pkgdir}/usr/bin/cgoban3"
}
