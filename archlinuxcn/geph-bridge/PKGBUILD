# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=geph-bridge
pkgver=0.20.2
pkgrel=1
pkgdesc='Runs on bridge nodes, which relay client-to-exit encrypted traffic across harsh firewalls'
arch=('x86_64')
url="https://github.com/geph-official/geph2"
license=('GPL3')
groups=('geph2')
depends=('glibc')
makedepends=('go-pie')
source=("$pkgname-$pkgver.tar.gz::https://github.com/geph-official/geph2/archive/v$pkgver.tar.gz")
sha512sums=('7170f31d5a9549d47b9e9582825925b6c04f45af2a8fb78a63f6f1885ab36bc2f97385b9155bfa5aa96445143a533b929f89eef9c0a2d5b986078ee2726b062d')

build() {
    cd "geph2-$pkgver/cmd/$pkgname/"
    go build
}

package() {
    install -Dm 644 "geph2-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm 755 "geph2-$pkgver/cmd/$pkgname/$pkgname" "$pkgdir/usr/bin/$pkgname"
}
