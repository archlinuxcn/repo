# Maintainer: Ye Jingchen <ye.jingchen@gmail.com>

pkgname=ttf-sarasa-gothic
pkgver=0.5.2
pkgrel=1
pkgdesc="A Chinese & Japanese programming font based on Iosevka and Source Han Sans (TTC)"
arch=('any')
url="https://github.com/be5invis/Sarasa-Gothic"
license=('BSD')
depends=('fontconfig' 'xorg-font-utils')
source=("https://github.com/be5invis/Sarasa-Gothic/releases/download/v$pkgver/sarasa-gothic-ttc-$pkgver.7z"
        "https://github.com/be5invis/Sarasa-Gothic/raw/master/LICENSE")
sha256sums=('7ebfc7a5037809d8c4730d8861bfdfb0483f515b3166fb9b5a8812736000d2b9'
            'SKIP')

package() {
	install -d "$pkgdir/usr/share/fonts/TTC"
	install -m644 "$srcdir/"*.ttc "$pkgdir/usr/share/fonts/TTC"
	install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
