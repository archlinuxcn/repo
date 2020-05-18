# Contributor: BluePeril <blueperil (at) blueperil _dot_ de>

pkgname=jcloisterzone
pkgver=4.5.1
pkgrel=1
pkgdesc="A Java version of the Carcassonne board game."
arch=('any')
url="http://jcloisterzone.com/en/"
license=('AGPL')
depends=('java-runtime>=8')
source=("http://play.jcloisterzone.com/builds/JCloisterZone-${pkgver}.tgz"
        'jcloisterzone.sh'
        'jcloisterzone.desktop'
        'ico.png')
sha256sums=('2fe141b7b4835219a8681212fd2be52c763f6bf933f6153a2614c3f442daed7b'
            'a7da7c81041d2e34fed08b4b10e27f32655095dc2246bb98b4db4feb48a3e05d'
            '7b25dfcdcb9ec286555a5f03e7b16bbc9c71f117f10aefc79b7e4537a72f4253'
            '012a090df7f1fa30fe3ede444eab92cb2f6fd3c37e1b6786f04da9feb3f7cf38')

package() {
    install -d "$pkgdir/usr/share"
    cp -r "$srcdir/JCloisterZone" "$pkgdir/usr/share/"
    find $pkgdir -type d -exec chmod 755 {} \;
    find $pkgdir -type f -exec chmod 644 {} \;
    install -D -m755 "$srcdir/${pkgname}.sh" "$pkgdir/usr/bin/${pkgname}"
    install -D -m644 "$srcdir/${pkgname}.desktop" "$pkgdir/usr/share/applications/${pkgname}.desktop"
    install -D -m644 "$srcdir/ico.png" "$pkgdir/usr/share/pixmaps/${pkgname}.png"
}

# vim:set ts=2 sw=2 et:
