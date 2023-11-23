# Maintainer: Jack Wu <self@origincode.me>

pkgname=zorin-desktop-themes
pkgver=4.1
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
sha512sums=('fb79eab5d8c1f9778c68c39aee52204a69aa734df3d70f702238a76e17ba448c442ca4c092961aa04d4f7ce3a36ed6c313d164c16a3ceaf19951396cc14fc674')

package() {
    cd "$pkgname-$pkgver"
    
    install -dm755 "$pkgdir/usr/share/themes"
    for theme in $(ls --hide={debian,LICENSE,README.md})
    do
        cp -r $theme "$pkgdir/usr/share/themes/"
    done
}
