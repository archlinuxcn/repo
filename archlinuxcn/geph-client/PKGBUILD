# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=geph-client
pkgver=0.20.2
pkgrel=3
pkgdesc='A command-line Geph client'
arch=('x86_64')
url="https://github.com/geph-official/geph2"
license=('GPL3')
groups=('geph2')
depends=('glibc')
makedepends=('go-pie')
source=("$pkgname-$pkgver.tar.gz::https://github.com/geph-official/geph2/archive/v$pkgver.tar.gz"
        "geph-client.service")
sha512sums=('7170f31d5a9549d47b9e9582825925b6c04f45af2a8fb78a63f6f1885ab36bc2f97385b9155bfa5aa96445143a533b929f89eef9c0a2d5b986078ee2726b062d'
            '925109cf7392f2bce01d59bc0bd6e2d7102670b5438fee5962c11b29646722c3bb905db439ba244310e8333465791e5eac979c3c2ead1536fe40d3dbb920333d')

build() {
    cd "geph2-$pkgver/cmd/$pkgname/"
    go build
}

package() {
    install -Dm 644 "geph2-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

    cd "geph2-$pkgver/cmd/$pkgname/"
    install -Dm 755 "$pkgname" "$pkgdir/usr/bin/$pkgname"

    install -d "$pkgdir/etc/geph2/"
    "$pkgdir/usr/bin/$pkgname" -dumpflags > "$pkgdir/etc/geph2/$pkgname.ini"

    install -Dm 644 "$srcdir/$pkgname.service" "$pkgdir/usr/lib/systemd/system/$pkgname.service"
    sed 's/geph-client.ini/%i.ini/' "$srcdir/$pkgname.service" -i
    install -Dm 644 "$srcdir/$pkgname.service" "$pkgdir/usr/lib/systemd/system/$pkgname@.service"
}
