# Maintainer: Jack Wu <self@origincode.me>

pkgname=zorin-desktop-themes
pkgver=4.0.7
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
sha512sums=('79668884513f00214601b4da0aac3d802f5dc5ddce80cd69ed604aee63c50acc16412a326d2373f35758180f42ddaa5c56989297e908a8b6bba4d59338015c20')

package() {
    cd "$pkgname-$pkgver"
    
    install -dm755 "$pkgdir/usr/share/themes"
    for theme in $(ls --hide={debian,LICENSE,README.md})
    do
        cp -r $theme "$pkgdir/usr/share/themes/"
    done
}
