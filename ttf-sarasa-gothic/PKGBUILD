# Maintainer: Ye Jingchen <ye.jingchen@gmail.com>

pkgname=ttf-sarasa-gothic
pkgver=0.5.4
pkgrel=1
pkgdesc="A Chinese & Japanese programming font based on Iosevka and Source Han Sans (TTC)"
arch=('any')
url="https://github.com/be5invis/Sarasa-Gothic"
license=('custom:SIL Open Font License v1.1')
depends=('fontconfig' 'xorg-font-utils')
source=("https://github.com/be5invis/Sarasa-Gothic/releases/download/v$pkgver/sarasa-gothic-ttc-$pkgver.7z"
        "https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/master/LICENSE")
sha256sums=('8b182e16942284e0a3f06208fc881d6f7b2b285cc233f0631a2a4b7b2fe75015'
            'SKIP')

package() {
	install -d "$pkgdir/usr/share/fonts/TTC"
	install -m644 "$srcdir/"*.ttc "$pkgdir/usr/share/fonts/TTC"
	install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
