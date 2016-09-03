# Maintainer: Mario Finelli <mario dot finelli at yahoo dot com>
# Contributor: Limao Luo <luolimao+AUR at gmail dot com>

pkgname=xfce-theme-blackbird
_pkgname=Blackbird
pkgver=0.4
pkgrel=2
pkgdesc="Dark Desktop Suite for Xfce."
arch=(any)
url="https://github.com/shimmerproject/Blackbird"
license=(CCPL:by-sa-3.0 GPL)
depends=(gtk-engine-murrine)
optdepends=('elementary-xfce-icons: matching icon set; use the dark icon theme'
    'gtk-engine-unico: required for gtk3 support')
source=($pkgname-$pkgver.tar.gz::https://github.com/shimmerproject/$_pkgname/archive/v$pkgver.tar.gz)
sha256sums=('ca31362254df2d336b2b090deb925f19a1dba72632ed9c7f82cf406be89ec1e6')

package() {
    install -d "$pkgdir"/usr/share/themes/
    cp -rf $_pkgname-$pkgver/ "$pkgdir"/usr/share/themes/$_pkgname/
    rm "$pkgdir"/usr/share/themes/$_pkgname/.gitignore
}
