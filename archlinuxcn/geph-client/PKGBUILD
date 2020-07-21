# Maintainer: Dct Mei <dctxmei@gmail.com>
# Co-Maintainer: xosdy <xosdy.t@gmail.com>
# Co-Maintainer: ohmyarch <ohmyarchlinux@protonmail.com>

pkgname=geph-client
pkgver=0.22.2
pkgrel=3
pkgdesc='A command-line Geph client'
arch=('x86_64')
url="https://github.com/geph-official/geph2"
license=('GPL3')
groups=('geph2')
depends=('glibc')
makedepends=('go')
backup=("etc/geph2/$pkgname.ini")
source=("$pkgname-$pkgver.tar.gz::https://github.com/geph-official/geph2/archive/v$pkgver.tar.gz"
        "geph-client.service")
sha512sums=('2595892671915e576aaee8a7a7beb4fbfb8b702520c6525cced9686c39516fa1c8aa38c360a50f7e698a90f68b23a4a24739903e6fbe8b6f695f0a89e5dc0de0'
            'fbbb29154a074c121abac3dd8e78768223b500b9cc5d9aa0c0608b79504c142242d08867cf86a5f8c0306f40662189e42a32274dcbdd4d5a186a4baddb3c2258')

build() {
    cd "geph2-$pkgver/cmd/$pkgname/"
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
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
