# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=geph-client
pkgver=0.19.1
pkgrel=2
pkgdesc='A command-line Geph client'
arch=('x86_64')
url="https://github.com/geph-official/geph2"
license=('GPL3')
groups=('geph2')
depends=('glibc')
makedepends=('go-pie')
source=("$pkgname-$pkgver.tar.gz::https://github.com/geph-official/geph2/archive/v$pkgver.tar.gz"
        "geph-client.service")
sha512sums=('f2f78083b794e9a7861c1448d6ea8204b63dc948784f96770e9c81edca5b9921b6903790924df1e6f5bc0e52c5cc6bf4c2c51fac43368cd8d455c92e55e652aa'
            '925109cf7392f2bce01d59bc0bd6e2d7102670b5438fee5962c11b29646722c3bb905db439ba244310e8333465791e5eac979c3c2ead1536fe40d3dbb920333d')

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
