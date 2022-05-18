# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname="font-victor-mono"
pkgver=1.5.3
pkgrel=1
pkgdesc="A programming font with cursive italics and ligatures."
arch=(any)
url="https://rubjo.github.io/victor-mono"
source=("victor-mono-$pkgver.zip::https://github.com/rubjo/victor-mono/raw/v$pkgver/public/VictorMonoAll.zip")
sha256sums=('839aa255ca6554430b6be353338431485e9c1452545c278161cc108a7ee7b1ab')

package() {
    cd "$srcdir"

    install -d "$pkgdir/usr/share/fonts/${pkgname%-fonts}"
    install -t "$pkgdir/usr/share/fonts/${pkgname%-fonts}" -m644 TTF/*.ttf
    install -Dm644 "LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

