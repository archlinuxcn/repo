# Maintainer: heavysink <winstonwu91@gmail.com>

pkgname=x88000
pkgver=1.5.1
pkgrel=1
pkgdesc="NEC - PC8801 Emulator on the Linux platform "
arch=('i686' 'x86_64')
url="http://www.cug.net/~manuke/x88000.html"
license=('GPL')
depends=('gtk2' 'libx11')
makedepends=('pkg-config')
source=("http://www.cug.net/~manuke/x88_1_5_1_src.tar.gz")
md5sums=('3dc2bb8c62ddb2a9a453024ac1662035')

build() {
        cd "$srcdir/x88_1_5_1_src"
        make
}

package() {
        cd "$srcdir/x88_1_5_1_src"
        install -d "$pkgdir/usr/bin"
        install -Dm755 "$srcdir/x88_1_5_1_src/X88000" "$pkgdir/usr/bin/X88000"
}