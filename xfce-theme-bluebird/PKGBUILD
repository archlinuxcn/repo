# Maintainer: Mario Finelli <mario dot finelli at yahoo dot com>
# Contributor: Limao Luo <luolimao+AUR at gmail dot com>

pkgname=xfce-theme-bluebird
_pkgname=Bluebird
pkgver=1.2
pkgrel=3
pkgdesc="A light blue Xfce theme, introduced in the release of Xubuntu 10.10."
arch=(any)
url=http://shimmerproject.org/projects/bluebird/
license=(CCPL:by-sa-3.0 GPL)
depends=(gtk-engine-murrine)
optdepends=('elementary-xfce-icons: matching icon set; use the dark icon theme'
    'gtk-engine-unico: required for gtk3 support'
    'shimmer-wallpapers: contains the Bluebird wallpaper, among others')
source=($pkgname-$pkgver.tar.gz::https://github.com/shimmerproject/$_pkgname/archive/v$pkgver.tar.gz)
sha256sums=('f76520181d9cb74a0cf1c61728ab02a7fb5f0835fef036ebd68f1e89caa0c579')

package() {
    install -d "$pkgdir"/usr/share/themes/
    cp -rf $_pkgname-$pkgver/ "$pkgdir"/usr/share/themes/$_pkgname/
    rm "$pkgdir"/usr/share/themes/$_pkgname/.gitignore
}
