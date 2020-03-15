# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=geph-client
pkgver=0.18.16
pkgrel=1
pkgdesc='A command-line Geph client'
arch=('x86_64')
url="https://github.com/geph-official/geph2"
license=('GPL3')
groups=('geph2')
depends=('glibc')
makedepends=('go-pie')
source=("$pkgname-$pkgver.tar.gz::https://github.com/geph-official/geph2/archive/v$pkgver.tar.gz")
sha512sums=('8493a98af3c04952ccba4b20d0a505e9e047f839d472161c0744a763ced78ebf7e34aebcbb317636d10d5547029362078bef431cb59c94fd38925bb69368d364')

build() {
    cd "geph2-$pkgver/cmd/$pkgname"
    go build
}

package() {
    cd "geph2-$pkgver/cmd/$pkgname"
    install -Dm 755 $pkgname "$pkgdir/usr/bin/$pkgname"
}
