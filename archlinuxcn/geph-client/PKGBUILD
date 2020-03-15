# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=geph-client
pkgver=0.18.16
pkgrel=2
pkgdesc='A command-line Geph client'
arch=('x86_64')
url="https://github.com/geph-official/geph2"
license=('GPL3')
groups=('geph2')
depends=('glibc')
makedepends=('go-pie')
install=$pkgname.install
source=("$pkgname-$pkgver.tar.gz::https://github.com/geph-official/geph2/archive/v$pkgver.tar.gz"
        "geph-client.service")
sha512sums=('8493a98af3c04952ccba4b20d0a505e9e047f839d472161c0744a763ced78ebf7e34aebcbb317636d10d5547029362078bef431cb59c94fd38925bb69368d364'
            'd23b669396f8bd6c99d78a478de233b211f4202812348dc2c78050ad2646870027a766a0bca51ead70b06947fb6dc49d646e462682e0d3fb685b3a00840d104a')

build() {
    cd "geph2-$pkgver/cmd/$pkgname"
    go build
}

package() {
    cd "geph2-$pkgver/cmd/$pkgname"
    install -Dm 755 "$pkgname" "$pkgdir/usr/bin/$pkgname"

    install -d "$pkgdir/etc/geph2"
    "$pkgdir/usr/bin/$pkgname" -dumpflags > "$pkgdir/etc/geph2/$pkgname.ini"

    install -Dm 644 "$srcdir/$pkgname.service" "$pkgdir/usr/lib/systemd/system/$pkgname.service"
    sed 's/geph-client.ini/%i.ini/' "$srcdir/$pkgname.service" -i
    install -Dm 644 "$srcdir/$pkgname.service" "$pkgdir/usr/lib/systemd/system/$pkgname@.service"
}
