# Maintainer: Ye Jingchen <ye.jingchen@gmail.com>
# Co-Maintainer: Markus Weimar <mail@markusweimar.de>

pkgname=ttf-sarasa-gothic
pkgver=0.9.0
pkgrel=1
pkgdesc="A Chinese & Japanese programming font based on Iosevka and Source Han Sans (TTC)"
arch=('any')
url="https://github.com/be5invis/Sarasa-Gothic"
license=('custom:SIL Open Font License v1.1')
depends=('fontconfig' 'xorg-font-utils')
source=("https://github.com/be5invis/Sarasa-Gothic/releases/download/v$pkgver/sarasa-gothic-ttc-$pkgver.7z"
        'https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/master/LICENSE')
sha256sums=('285f1621b43fc68624987f60faf8dfb2cc2a582cde6c31fd8ebd5269915ef2d9'
            '15d8d7964167f8ec518783801c809991807804cfde691242471e24ce66de6934')

package() {
    install -d "$pkgdir/usr/share/fonts/${pkgname:4}"
    install -m644 "$srcdir/"*.ttc "$pkgdir/usr/share/fonts/${pkgname:4}"
    install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
