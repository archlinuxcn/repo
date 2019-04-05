# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=ariang-allinone
pkgver=1.0.2
pkgrel=1
pkgdesc="AriaNg, a modern web frontend making aria2 easier to use. (all-in-one version)"
arch=('any')
url="https://github.com/mayswind/AriaNg"
license=('MIT')
depends=("xdg-utils")
source=("https://github.com/mayswind/AriaNg/releases/download/$pkgver/AriaNg-$pkgver-AllInOne.zip"
        "$pkgname")
sha512sums=("8499767ef1cdf28a9b7e4f09bb90c7c39fe883f3afa0b6277e6007b4e72316412dede809ebd68d1e23f661428cd9e0f465e7013ae5c3963345c2b166d93004e1"
            "17aed8ae60919025b45741f21ac9485546199003e9fa9c1414fbf2934cbffe090678e3bb2b3f22b2b7d112ac68123a483a0a1f41f9f6781dc98a55442db62af9")

package() {
    install -Dm 644 index.html "$pkgdir/usr/share/$pkgname/index.html"
    install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm 755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
}
