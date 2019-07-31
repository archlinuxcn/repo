# Maintainer: Jack Wu <origincoder@yahoo.com>

_pkgname=zorin-desktop-themes
pkgname=$_pkgname-git
pkgver=2.0.8.r0.g9c60813
pkgrel=1
pkgdesc="The Zorin OS desktop theme provided in a variety of color combinations."
arch=('any')
url="https://github.com/ZorinOS/zorin-desktop-themes"
license=('GPL2')
depends=()
makedepends=('git')
provides=('zorin-desktop-themes')
conflicts=('zorin-desktop-themes')
source=(
        "git+https://github.com/ZorinOS/zorin-desktop-themes.git"
)
md5sums=('SKIP')

pkgver() {
    cd "$_pkgname"
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

package() {
    cd "$_pkgname"
    
    install -dm755 "$pkgdir/usr/share/themes"
    for theme in $(ls --hide={debian,LICENSE,README.md})
    do
        cp -r $theme "$pkgdir/usr/share/themes/"
    done
}
