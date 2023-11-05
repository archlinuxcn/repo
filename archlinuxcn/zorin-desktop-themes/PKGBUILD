# Maintainer: Jack Wu <self@origincode.me>

pkgname=zorin-desktop-themes
pkgver=4.0.4
pkgrel=1
pkgdesc="The Zorin OS desktop theme provided in a variety of color combinations."
arch=('any')
url="https://github.com/ZorinOS/zorin-desktop-themes"
license=('GPL2')
depends=('gtk-engine-murrine')
makedepends=()
provides=('zorin-desktop-themes')
conflicts=('zorin-desktop-themes-git')
source=(
        "$pkgname-$pkgver.tar.gz::https://github.com/ZorinOS/$pkgname/archive/$pkgver.tar.gz"
)
sha512sums=('311ce428c49860e967e8a6ec0b2b4551154089e1c117f8bf4c46f1e97b5e127bd1889d2dd64318a26877a032cbb090cb492e71448add2869b99c0087cd5c49f0')

package() {
    cd "$pkgname-$pkgver"
    
    install -dm755 "$pkgdir/usr/share/themes"
    for theme in $(ls --hide={debian,LICENSE,README.md})
    do
        cp -r $theme "$pkgdir/usr/share/themes/"
    done
}
