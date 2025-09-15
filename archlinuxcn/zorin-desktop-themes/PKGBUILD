# Maintainer: Jack Wu <self@origincode.me>

pkgname=zorin-desktop-themes
pkgver=5.1
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
sha512sums=('23a3c1b3beeb73ef60a81361cce73b19eef65bc816e33cdab215be5fe5347735b425d99116677325344bcd6418de0a66bce280332ed60f4bbb20f09570d33c02')

package() {
    cd "$pkgname-$pkgver"
    
    install -dm755 "$pkgdir/usr/share/themes"
    for theme in $(ls --hide={debian,LICENSE,README.md})
    do
        cp -r $theme "$pkgdir/usr/share/themes/"
    done
}
