# Maintainer: Jack Wu <self@origincode.me>

pkgname=zorin-desktop-themes
pkgver=4.0.9
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
sha512sums=('0d525d7b078ceac2c7431e28697d9ed9b6a96d00f08615e6a2e6f74785a788354aa108bb620b7b76d266337e5ed4df4b7e3d812fd7ff7075e0a864a35255782b')

package() {
    cd "$pkgname-$pkgver"
    
    install -dm755 "$pkgdir/usr/share/themes"
    for theme in $(ls --hide={debian,LICENSE,README.md})
    do
        cp -r $theme "$pkgdir/usr/share/themes/"
    done
}
