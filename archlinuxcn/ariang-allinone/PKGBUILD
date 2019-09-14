# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=ariang-allinone
pkgver=1.1.3
pkgrel=1
pkgdesc="AriaNg, a modern web frontend making aria2 easier to use. (all-in-one version)"
arch=('any')
url="https://github.com/mayswind/AriaNg"
license=('MIT')
depends=('bash')
source=("https://github.com/mayswind/AriaNg/releases/download/$pkgver/AriaNg-$pkgver-AllInOne.zip"
        "$pkgname.sh")
sha512sums=('067768027f9ecc2c549e609de3acbe18038d5304fbccec4a794283ef5ab86f689111a93ce30d8693472f0979def3807deb33e1dd79968bd8f61e6220883cf3a4'
            '035a1e360e0ef94540eedfe98dc30d2683a0c07d0e68a5eaeff3c0662b00273e117ff3b59a29f18df7cda9a0a931070c5f08436da441df00cd7913a4f4bbdb1d')

package() {
    install -Dm 644 index.html "$pkgdir/usr/share/$pkgname/index.html"
    install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm 755 "$pkgname.sh" "$pkgdir/usr/bin/$pkgname"
}
