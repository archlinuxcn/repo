# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=ariang-allinone
pkgver=1.1.1
pkgrel=1
pkgdesc="AriaNg, a modern web frontend making aria2 easier to use. (all-in-one version)"
arch=('any')
url="https://github.com/mayswind/AriaNg"
license=('MIT')
depends=('bash')
source=("https://github.com/mayswind/AriaNg/releases/download/$pkgver/AriaNg-$pkgver-AllInOne.zip"
        "$pkgname.sh")
sha512sums=('2e8329816a809faec5adac42ee5df3504e4dbc5dc084a423f371a3a64fe0b32adf6a24dcf29d31ad8f8e0fa37804cd1044a935409dcd77278794bfe1c07159ea'
            '035a1e360e0ef94540eedfe98dc30d2683a0c07d0e68a5eaeff3c0662b00273e117ff3b59a29f18df7cda9a0a931070c5f08436da441df00cd7913a4f4bbdb1d')

package() {
    install -Dm 644 index.html "$pkgdir/usr/share/$pkgname/index.html"
    install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm 755 "$pkgname.sh" "$pkgdir/usr/bin/$pkgname"
}
