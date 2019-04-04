# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=music-dl
pkgver=2.2.0
pkgrel=1
pkgdesc="Music-dl is a command line tool which helps you search and download music from multiple sources"
arch=('any')
url="https://github.com/0xHJK/music-dl"
license=('MIT')
depends=("python-click" "python-requests" "python-pycryptodome" "python-prettytable")
source=("$pkgname-$pkgver.tar.gz::https://github.com/0xHJK/music-dl/archive/v$pkgver.tar.gz")
sha512sums=("b6b59e32a8e524fc7b046ada8e87667155ad9d9ae0e3da930bbd067dcc56548a3f728559f2f92cd2a6509e411d250e2d91876011d1bd8ad0656d68741a020da5")

build() {
    cd "$srcdir/$pkgname-$pkgver"
    python setup.py build
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
    install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
