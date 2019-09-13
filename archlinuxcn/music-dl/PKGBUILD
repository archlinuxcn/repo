# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=music-dl
pkgver=3.0.0
pkgrel=1
pkgdesc="A command line tool which helps you search and download music from multiple sources"
arch=('any')
url="https://github.com/0xHJK/music-dl"
license=('MIT')
depends=("python-click" "python-requests" "python-pycryptodome" "python-prettytable")
source=("$pkgname-$pkgver.tar.gz::https://github.com/0xHJK/music-dl/archive/v$pkgver.tar.gz")
sha512sums=("2fc420bc8a2931a97191ebce18fbb5fc490d399f46bc02f153203283dc1ae4b1da11c624cc33c69fd3ac4fd7a7b0c24ee75fdde04b6cbdb9e5930b43c14c3098")

build() {
    cd "$srcdir/$pkgname-$pkgver"
    python setup.py build
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
    rm "$pkgdir/usr/LICENSE"
    rm "$pkgdir/usr/README.en.md"
    install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm 644 README.en.md "$pkgdir/usr/share/$pkgname/README"
}
