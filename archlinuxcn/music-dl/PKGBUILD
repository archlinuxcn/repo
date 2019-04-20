# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=music-dl
pkgver=2.2.1
pkgrel=1
pkgdesc="Music-dl is a command line tool which helps you search and download music from multiple sources"
arch=('any')
url="https://github.com/0xHJK/music-dl"
license=('MIT')
depends=("python-click" "python-requests" "python-pycryptodome" "python-prettytable")
source=("$pkgname-$pkgver.tar.gz::https://github.com/0xHJK/music-dl/archive/v$pkgver.tar.gz")
sha512sums=("74a8c31b341d9da7d997138f743c383fb7b5994dc340dcd4b8ff5d319b8e86f74fcb796a611be316eaa8f62bad26dd0e553dcf003c8ffd288ebd270f697546eb")

build() {
    cd "$srcdir/$pkgname-$pkgver"
    python setup.py build
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
    install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
