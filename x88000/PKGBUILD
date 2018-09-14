# Maintainer: heavysink <winstonwu91@gmail.com>

pkgname=x88000
pkgver=1.5.3
pkgrel=3
pkgdesc="NEC - PC8801 Emulator on the Linux platform "
arch=('i686' 'x86_64')
url="http://www.cug.net/~manuke/x88000.html"
license=('GPL')
depends=('gtk2' 'libx11')
makedepends=('pkg-config')
source=("http://www.cug.net/~manuke/x88_${pkgver//./_}_src.tar.gz")
md5sums=('5169d560421a082d6d7671b1a3c8c38e')

build() {
        cd "$srcdir/x88_${pkgver//./_}_src"
        make
}

package() {
        cd "$srcdir/x88_${pkgver//./_}_src"
        install -d "$pkgdir/usr/bin"
        install -Dm755 "$srcdir/x88_${pkgver//./_}_src/X88000" "$pkgdir/usr/bin/X88000"
}
