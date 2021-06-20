# Maintainer: Luca Weiss <luca (at) z3ntu (dot) xyz>

pkgname=lmdbxx
pkgver=1.0.0
pkgrel=1
pkgdesc="C++17 wrapper for the LMDB embedded B+ tree database library"
arch=('any')
url="https://github.com/hoytech/lmdbxx"
license=('custom:Public Domain')
depends=('lmdb')
source=("https://github.com/hoytech/lmdbxx/archive/$pkgver/lmdbxx-$pkgver.tar.gz")
sha512sums=('54f6c4863273b4de8aed6bc19f353c7a66d8ae633198e9784c55cea8e54460e4030ebe45e91a7c820aade084933f21cd4193ef8c04bb2aef11bf252281404171')

package() {
    cd "$pkgname-$pkgver"
    make PREFIX=/usr DESTDIR="$pkgdir/" install
    install -m644 -D UNLICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
