# Maintainer: Jack Wu <origincoder@yahoo.com>

pkgname=zorin-desktop-themes
pkgver=2.0.8
pkgrel=1
pkgdesc="The Zorin OS desktop theme provided in a variety of color combinations."
arch=('any')
url="https://github.com/ZorinOS/zorin-desktop-themes"
license=('GPL2')
depends=()
makedepends=()
provides=('zorin-desktop-themes')
conflicts=('zorin-desktop-themes-git')
source=(
        "$pkgname-$pkgver.tar.xz::https://github.com/ZorinOS/$pkgname/archive/$pkgver.tar.gz"
)
md5sums=('49aa573993a5dd0733ecee77bda88d3a')

package() {
    cd "$pkgname-$pkgver"
    
    install -dm755 "$pkgdir/usr/share/themes"
    for theme in $(ls --hide={debian,LICENSE,README.md})
    do
        cp -r $theme "$pkgdir/usr/share/themes/"
    done
}
