# Contributor: BluePeril <blueperil (at) blueperil _dot_ de>

pkgname=jcloisterzone
pkgver=4.4.1
pkgrel=1
pkgdesc="A Java version of the Carcassonne board game."
arch=('any')
url="http://jcloisterzone.com/en/"
license=('AGPL')
depends=('java-runtime>=8' 'archlinux-java-run')
source=("http://play.jcloisterzone.com/builds/JCloisterZone-${pkgver}.tgz"
        'jcloisterzone.sh'
        'jcloisterzone.desktop'
        'ico.png')
sha256sums=('ade67e2f6855ecb630fa3b3b8ce69e57af179538254f5c344a501fbf8465d325'
            '47f628afde304e1e6f090cd093f7b5b3027d339a085f129c1c8201b64a17fe9d'
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
