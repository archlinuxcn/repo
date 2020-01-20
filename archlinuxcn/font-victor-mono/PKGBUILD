pkgname="font-victor-mono"
pkgver=1.3.1
pkgrel=1
pkgdesc="A programming font with cursive italics and ligatures."
arch=(any)
url="https://rubjo.github.io/victor-mono"
source=(
    "victor-mono-$pkgver.zip::https://github.com/rubjo/victor-mono/raw/v$pkgver/public/VictorMonoAll.zip"
)
sha256sums=(
    "2fb18068fb921e4580e96540f2626c0c4b033eae8da35dd892e5a9ce52cd0ed9"
)

package() {
    cd "$srcdir"

    install -d "$pkgdir/usr/share/fonts/${pkgname%-fonts}"
    install -t "$pkgdir/usr/share/fonts/${pkgname%-fonts}" -m644 TTF/*.ttf
    install -Dm644 "LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

