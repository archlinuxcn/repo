# Maintainer: Mario Finelli <mario dot finelli at yahoo dot com>
# Contributor: Limao Luo <luolimao+AUR at gmail dot com>

pkgname=xfce-theme-albatross
_pkgname=Albatross
pkgver=1.7.4
pkgrel=1
pkgdesc="A dark, smooth Xfce theme, introduced in the release of Xubuntu 9.10."
arch=(any)
url=http://shimmerproject.org/projects/albatross/
license=(CCPL:by-sa-3.0 GPL)
depends=(gtk-engine-murrine)
optdepends=('elementary-xfce-icons: matching icon set; use the dark icon theme'
    'gtk-engine-unico: required for gtk3 support'
    'shimmer-wallpapers: contains the Albatross wallpaper, among others')
source=($pkgname-$pkgver.tar.gz::https://github.com/shimmerproject/$_pkgname/archive/v$pkgver.tar.gz)
sha256sums=('ff40e28e164cb99f01b131ae3e79a07782e29a720535460e901ce305fa322ae1')

package() {
    install -d "$pkgdir"/usr/share/themes/
    cp -rf $_pkgname-$pkgver/ "$pkgdir"/usr/share/themes/$_pkgname/
    rm "$pkgdir"/usr/share/themes/$_pkgname/.gitignore
}
