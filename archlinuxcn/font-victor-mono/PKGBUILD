pkgname="font-victor-mono"
pkgver=1.4.2
pkgrel=1
pkgdesc="A programming font with cursive italics and ligatures."
arch=(any)
url="https://rubjo.github.io/victor-mono"
source=(
    "victor-mono-$pkgver.zip::https://github.com/rubjo/victor-mono/raw/v$pkgver/public/VictorMonoAll.zip"
)
sha256sums=(
    "75eeeeff533b6011eac4591523400e05ad436d07eeea3f37ab4234a0e4064604"
)

package() {
    cd "$srcdir"

    install -d "$pkgdir/usr/share/fonts/${pkgname%-fonts}"
    install -t "$pkgdir/usr/share/fonts/${pkgname%-fonts}" -m644 TTF/*.ttf
    install -Dm644 "LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

