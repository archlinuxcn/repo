# Maintainer: Sven-Hendrik Haase <svenstaro@gmail.com>
pkgname=genact
pkgver=0.10.0
pkgrel=1
pkgdesc="A nonsense activity generator"
url="https://github.com/svenstaro/genact"
arch=("x86_64")
license=("MIT")
depends=('gcc-libs')
makedepends=("rust")
source=("$pkgname-$pkgver.tar.gz::https://github.com/svenstaro/$pkgname/archive/v$pkgver.tar.gz")
sha512sums=('75a270b6ca70d496057611d32097cf1c52b756d4bff80e5f93398f7ad4ecb4bf73864605a606efa9c146be4145a9f87028290046cb343445e52105908e5c795f')

build() {
    cd "$srcdir/$pkgname-$pkgver"
    cargo build --release --locked
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    install -Dm 644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm 755 "target/release/$pkgname" "$pkgdir/usr/bin/$pkgname"
}
