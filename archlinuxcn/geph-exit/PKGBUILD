# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=geph-exit
pkgver=0.20.2
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
sha512sums=('7170f31d5a9549d47b9e9582825925b6c04f45af2a8fb78a63f6f1885ab36bc2f97385b9155bfa5aa96445143a533b929f89eef9c0a2d5b986078ee2726b062d'
            'eba4c6ab19ff26cccd678043adb8563f6e02336959a8b923bac31b7dafcf04ec8b9b1c6cb1def26253871f4654c06b797ec1aa16500e58035bc44fb7cbffa025')

build() {
    cd "geph2-$pkgver/cmd/$pkgname/"
    go build
}

package() {
    install -Dm 644 "geph2-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm 755 "geph2-$pkgver/cmd/$pkgname/$pkgname" "$pkgdir/usr/bin/$pkgname"
    install -Dm 644 "$srcdir/$pkgname.service" "$pkgdir/usr/lib/systemd/system/$pkgname.service"
}
