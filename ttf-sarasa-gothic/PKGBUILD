# Maintainer: Ye Jingchen <ye.jingchen@gmail.com>
# Co-Maintainer: Markus Weimar <mail@markusweimar.de>

pkgname=ttf-sarasa-gothic
pkgver=0.7.0
pkgrel=1
pkgdesc="A Chinese & Japanese programming font based on Iosevka and Source Han Sans (TTC)"
arch=('any')
url="https://github.com/be5invis/Sarasa-Gothic"
license=('custom:SIL Open Font License v1.1')
depends=('fontconfig' 'xorg-font-utils')
source=("https://github.com/be5invis/Sarasa-Gothic/releases/download/v$pkgver/sarasa-gothic-ttc-$pkgver.7z"
        'https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/master/LICENSE')
sha256sums=('9cd9fbdc741c99590a8b76feb2da4cda49695f148107df338a0eb57f6edc3dd3'
            '15d8d7964167f8ec518783801c809991807804cfde691242471e24ce66de6934')

package() {
    install -d "$pkgdir/usr/share/fonts/TTC"
    install -m644 "$srcdir/"*.ttc "$pkgdir/usr/share/fonts/TTC"
    install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
