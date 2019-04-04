# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=ariang-allinone
pkgver=1.0.1
pkgrel=1
pkgdesc="AriaNg, a modern web frontend making aria2 easier to use. (all-in-one version)"
arch=('any')
url="https://github.com/mayswind/AriaNg"
license=('MIT')
depends=("xdg-utils")
source=("https://github.com/mayswind/AriaNg/releases/download/$pkgver/AriaNg-$pkgver-AllInOne.zip"
        "$pkgname")
sha512sums=("dfcd2351a2fa35420fea19a02d742fc4347ffb0afef1711d9510b00f118a3c514115011fbeaa0637b7a68bdcf19e128bf61453333a90e940d16df4e670c26132"
            "17aed8ae60919025b45741f21ac9485546199003e9fa9c1414fbf2934cbffe090678e3bb2b3f22b2b7d112ac68123a483a0a1f41f9f6781dc98a55442db62af9")

package() {
    install -Dm 644 index.html "$pkgdir/usr/share/$pkgname/index.html"
    install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm 755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
}
