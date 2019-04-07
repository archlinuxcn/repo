# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=ariang-allinone
pkgver=1.0.2
pkgrel=3
pkgdesc="AriaNg, a modern web frontend making aria2 easier to use. (all-in-one version)"
arch=('any')
url="https://github.com/mayswind/AriaNg"
license=('MIT')
depends=("xdg-utils")
source=("https://github.com/mayswind/AriaNg/releases/download/$pkgver/AriaNg-$pkgver-AllInOne.zip"
        "$pkgname")
sha512sums=("6495676ae9b2c5b4e67861561c1a4144630e88e0f9e937e60c459339b4b80db51a22b9d05759fb8aa372378dbca5b2edcd01796097ac40de8bd11ec1704de3af"
            "17aed8ae60919025b45741f21ac9485546199003e9fa9c1414fbf2934cbffe090678e3bb2b3f22b2b7d112ac68123a483a0a1f41f9f6781dc98a55442db62af9")

package() {
    install -Dm 644 index.html "$pkgdir/usr/share/$pkgname/index.html"
    install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm 755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
}
