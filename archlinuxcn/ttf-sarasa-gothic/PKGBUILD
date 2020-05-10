# Maintainer: Ye Jingchen <ye.jingchen@gmail.com>
# Co-Maintainer: Markus Weimar <mail@markusweimar.de>

pkgname=ttf-sarasa-gothic
pkgver=0.12.6
pkgrel=1
pkgdesc="A CJK programming font based on Iosevka and Source Han Sans. (TTC)"
arch=('any')
url="https://github.com/be5invis/Sarasa-Gothic"
license=('OFL')
provides=('ttf-sarasa-slab')
source=("https://github.com/be5invis/Sarasa-Gothic/releases/download/v$pkgver/sarasa-gothic-ttc-$pkgver.7z"
        "LICENSE-$pkgver::https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/v${pkgver}/LICENSE")
sha256sums=('0631b5b1e6c905b693a6ca25c0bdf19ec6c7ca7422bc01355c9049454b4bd3bc'
            '07e26208b78894948573d001a0133a8d071e161eba6ae65e2ab521fef311a429')

package() {
    install -d "$pkgdir/usr/share/fonts/${pkgname:4}"
    install -m644 "$srcdir/"*.ttc "$pkgdir/usr/share/fonts/${pkgname:4}"
    install -Dm644 "$srcdir/LICENSE-$pkgver" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
