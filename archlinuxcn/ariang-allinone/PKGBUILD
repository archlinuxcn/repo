# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=ariang-allinone
pkgver=1.1.0
pkgrel=1
pkgdesc="AriaNg, a modern web frontend making aria2 easier to use. (all-in-one version)"
arch=('any')
url="https://github.com/mayswind/AriaNg"
license=('MIT')
depends=("xdg-utils")
source=("https://github.com/mayswind/AriaNg/releases/download/$pkgver/AriaNg-$pkgver-AllInOne.zip"
        "$pkgname")
sha512sums=("f6a22534bf9ad4887f63c8b54c62b5c979b12a35488f3cd4768a3208261924de11e0a3c8b8dd3e9b564b650a7f0d57f1940551386d62c5b37abf467fd35f0bdc"
            "17aed8ae60919025b45741f21ac9485546199003e9fa9c1414fbf2934cbffe090678e3bb2b3f22b2b7d112ac68123a483a0a1f41f9f6781dc98a55442db62af9")

package() {
    install -Dm 644 index.html "$pkgdir/usr/share/$pkgname/index.html"
    install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm 755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
}
