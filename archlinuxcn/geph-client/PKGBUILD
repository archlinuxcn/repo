# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=geph-client
pkgver=0.21.4
pkgrel=1
pkgdesc='A command-line Geph client'
arch=('x86_64')
url="https://github.com/geph-official/geph2"
license=('GPL3')
groups=('geph2')
depends=('glibc')
makedepends=('go-pie')
source=("$pkgname-$pkgver.tar.gz::https://github.com/geph-official/geph2/archive/v$pkgver.tar.gz"
        "geph-client.service")
sha512sums=('aecf3bb0f5c6cec5a6db9ce9c11174686208f9caca16736a7addeb70e556446ebdb1384a95c6ee440bf8a583de9b609cb2bc1c8a5720a618024fe57b14d9cd18'
            'fbbb29154a074c121abac3dd8e78768223b500b9cc5d9aa0c0608b79504c142242d08867cf86a5f8c0306f40662189e42a32274dcbdd4d5a186a4baddb3c2258')

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
