# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=geph-bridge
pkgver=0.21.4
pkgrel=1
pkgdesc='Runs on bridge nodes, which relay client-to-exit encrypted traffic across harsh firewalls'
arch=('x86_64')
url="https://github.com/geph-official/geph2"
license=('GPL3')
groups=('geph2')
depends=('glibc')
makedepends=('go-pie')
source=("$pkgname-$pkgver.tar.gz::https://github.com/geph-official/geph2/archive/v$pkgver.tar.gz")
sha512sums=('aecf3bb0f5c6cec5a6db9ce9c11174686208f9caca16736a7addeb70e556446ebdb1384a95c6ee440bf8a583de9b609cb2bc1c8a5720a618024fe57b14d9cd18')

build() {
    cd "geph2-$pkgver/cmd/$pkgname/"
    go build
}

package() {
    install -Dm 644 "geph2-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm 755 "geph2-$pkgver/cmd/$pkgname/$pkgname" "$pkgdir/usr/bin/$pkgname"
}
