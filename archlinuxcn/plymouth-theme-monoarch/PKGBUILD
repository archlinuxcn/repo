# Maintainer: Marco Buzzanca <marco /DOT/ bzn /AT/ gmail /DOT/ com>
pkgname=plymouth-theme-monoarch
pkgver=0.1
pkgrel=1
pkgdesc='Monochrome Arch Linux theme for Plymouth'
arch=('any')
url='https://farsil.github.io/monoarch/'
license=('MIT')
depends=('plymouth')
install=$pkgname.install
source=("https://github.com/farsil/monoarch/archive/$pkgver.tar.gz"
        "$pkgname.install")
sha256sums=('e26fe7100dbe612b517037a55488f5ae25976b55e60a542c53623073e52a5ca1'
            'efc4134ab3a534dbd0b92ec1abc55f17cda2968c0d5c6a855fe0cb760b4b291a')

package() {
    cd "$srcdir/monoarch-$pkgver"

    install -d "$pkgdir/usr/share/plymouth/themes/monoarch/images/" 
    install -Dm644 monoarch.* "$pkgdir/usr/share/plymouth/themes/monoarch/"
    install -Dm644 images/* "$pkgdir/usr/share/plymouth/themes/monoarch/images/"
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
