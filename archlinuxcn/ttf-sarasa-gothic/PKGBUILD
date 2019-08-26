# Maintainer: Ye Jingchen <ye.jingchen@gmail.com>
# Co-Maintainer: Markus Weimar <mail@markusweimar.de>

pkgname=ttf-sarasa-gothic
pkgver=0.8.2
pkgrel=2
pkgdesc="A Chinese & Japanese programming font based on Iosevka and Source Han Sans (TTC)"
arch=('any')
url="https://github.com/be5invis/Sarasa-Gothic"
license=('custom:SIL Open Font License v1.1')
depends=('fontconfig' 'xorg-font-utils')
source=("https://github.com/be5invis/Sarasa-Gothic/releases/download/v$pkgver/sarasa-gothic-ttc-$pkgver.7z"
        'https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/master/LICENSE')
sha256sums=('f56434178c36a509c3ed757a1bb713d7cdfe94e55fe39e16a6991ee3205a5251'
            '15d8d7964167f8ec518783801c809991807804cfde691242471e24ce66de6934')

package() {
    install -d "$pkgdir/usr/share/fonts/${pkgname:4}"
    install -m644 "$srcdir/"*.ttc "$pkgdir/usr/share/fonts/${pkgname:4}"
    install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
