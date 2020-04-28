# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=geph-exit
pkgver=0.21.4
pkgrel=1
pkgdesc='Runs on highly secure exit nodes, and handles exit traffic'
arch=('x86_64')
url="https://github.com/geph-official/geph2"
license=('GPL3')
groups=('geph2')
depends=('glibc')
makedepends=('go-pie')
source=("$pkgname-$pkgver.tar.gz::https://github.com/geph-official/geph2/archive/v$pkgver.tar.gz"
        "geph-exit.service")
sha512sums=('aecf3bb0f5c6cec5a6db9ce9c11174686208f9caca16736a7addeb70e556446ebdb1384a95c6ee440bf8a583de9b609cb2bc1c8a5720a618024fe57b14d9cd18'
            '6d8f4c68a194ace0f70a68d3e3db9e8dac3f0d64a6de4e1551ec4e3554db9926da340ff487369a183dcb5e65046343d786893cda2ad6d786d879634193700d45')

build() {
    cd "geph2-$pkgver/cmd/$pkgname/"
    go build
}

package() {
    install -Dm 644 "geph2-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm 755 "geph2-$pkgver/cmd/$pkgname/$pkgname" "$pkgdir/usr/bin/$pkgname"
    install -Dm 644 "$srcdir/$pkgname.service" "$pkgdir/usr/lib/systemd/system/$pkgname.service"
}
