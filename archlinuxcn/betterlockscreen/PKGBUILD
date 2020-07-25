# Maintainer: Dct Mei <dctxmei@gmail.com>
# Contributor: AUTplayed <fips.hem@gmail.com>
# Contributor: pavanjadhaw <pavanjadhaw96@gmail.com>

pkgname=betterlockscreen
pkgver=3.0.1
pkgrel=5
pkgdesc="A simple, minimal lockscreen"
arch=('any')
url="https://github.com/pavanjadhaw/$pkgname"
license=('MIT')
depends=('feh' 'i3lock-color' 'imagemagick' 'xorg-xdpyinfo' 'xorg-xrandr')
conflicts=('betterlockscreen-git')
source=("$url/archive/$pkgver.tar.gz")
sha256sums=('9b80af4b93e0b35bc916a584522ecf9eb39414c8010a2e4f2bb6941fdc5faf28')

package() {
    cd "$pkgname-$pkgver"
    install -Dm 755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
    install -Dm 644 "$pkgname@.service" "$pkgdir/usr/lib/systemd/system/betterlockscreen@.service"
    install -Dm 644 "examples/${pkgname}rc" "$pkgdir/usr/share/doc/betterlockscreen/examples/${pkgname}rc"
    install -Dm 644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
