# Maintainer: Ye Jingchen <ye.jingchen@gmail.com>

pkgname=ttf-sarasa-gothic
pkgver=0.3.0
pkgrel=1
pkgdesc="A Chinese & Japanese programming font based on Iosevka and Source Han Sans"
arch=('any')
url="https://github.com/be5invis/Sarasa-Gothic"
license=('BSD')
depends=('fontconfig' 'xorg-font-utils')
source=("https://github.com/be5invis/Sarasa-Gothic/releases/download/v$pkgver/sarasa-gothic-ttc-$pkgver.7z"
        "https://github.com/be5invis/Sarasa-Gothic/raw/master/LICENSE")
sha256sums=('e9faa99fdf7057ee4b84d0890f1f0543745b20d4ed1161320cc100eb8d2bb187'
            'SKIP')

package() {
	install -d "$pkgdir/usr/share/fonts/TTC"
	install -m644 "$srcdir/"*.ttc "$pkgdir/usr/share/fonts/TTC"
	install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
