# Maintainer: Dct Mei <dctxmei@gmail.com>
# Co-Maintainer: xosdy <xosdy.t@gmail.com>
# Co-Maintainer: ohmyarch <ohmyarchlinux@protonmail.com>

pkgname=geph-exit
pkgver=0.22.2
pkgrel=1
pkgdesc='Runs on highly secure exit nodes, and handles exit traffic'
arch=('x86_64')
url="https://github.com/geph-official/geph2"
license=('GPL3')
groups=('geph2')
depends=('glibc')
makedepends=('go')
source=("$pkgname-$pkgver.tar.gz::https://github.com/geph-official/geph2/archive/v$pkgver.tar.gz"
        "geph-exit.service")
sha512sums=('2595892671915e576aaee8a7a7beb4fbfb8b702520c6525cced9686c39516fa1c8aa38c360a50f7e698a90f68b23a4a24739903e6fbe8b6f695f0a89e5dc0de0'
            '6d8f4c68a194ace0f70a68d3e3db9e8dac3f0d64a6de4e1551ec4e3554db9926da340ff487369a183dcb5e65046343d786893cda2ad6d786d879634193700d45')

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
    install -Dm 755 "geph2-$pkgver/cmd/$pkgname/$pkgname" "$pkgdir/usr/bin/$pkgname"
    install -Dm 644 "$srcdir/$pkgname.service" "$pkgdir/usr/lib/systemd/system/$pkgname.service"
}
