# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=ariang-allinone
pkgver=1.1.4
pkgrel=1
pkgdesc="AriaNg, a modern web frontend making aria2 easier to use. (all-in-one version)"
arch=('any')
url="https://github.com/mayswind/AriaNg"
license=('MIT')
depends=('bash')
source=("https://github.com/mayswind/AriaNg/releases/download/$pkgver/AriaNg-$pkgver-AllInOne.zip"
        "$pkgname.sh")
sha512sums=('e212f415b7ab4fb1f2efcd25094299f37f41b5c2dfac5718698ad0e859e35603147e499e00f9e8afc26376e7b1247a65731b960f5e27d182c4b274f9f4887128'
            '035a1e360e0ef94540eedfe98dc30d2683a0c07d0e68a5eaeff3c0662b00273e117ff3b59a29f18df7cda9a0a931070c5f08436da441df00cd7913a4f4bbdb1d')

package() {
    install -Dm 644 index.html "$pkgdir/usr/share/$pkgname/index.html"
    install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm 755 "$pkgname.sh" "$pkgdir/usr/bin/$pkgname"
}
