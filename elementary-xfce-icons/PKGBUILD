# Maintainer: mortzprk <mortz.prk@gmail.com>
# Contributor: Hugo Osvaldo Barrera <hugo@barrera.io>
# Contributor: Limao Luo <luolimao+AUR@gmail.com>
# Contributor: flan_suse <windows2linux@zoho.com>
# Contributor: auscompgeek <auscompgeek@zoho.com>

pkgname=elementary-xfce-icons
pkgver=0.9
pkgrel=1
pkgdesc='Elementary icons forked, extended and maintained for Xfce.'
arch=(any)
url=https://github.com/shimmerproject/elementary-xfce
license=(GPL2)
depends=(gnome-icon-theme)
options=(!strip)
conflicts=($pkgname-git)
optdepends=('xfce-theme-albatross: matching Shimmer Project Xfce theme'
            'xfce-theme-bluebird: matching Shimmer Project Xfce theme'
            'xfce-theme-greybird: matching Shimmer Project Xfce theme')
source=($pkgname-$pkgver.tar.gz::https://github.com/shimmerproject/${pkgname%-*}/archive/v$pkgver.tar.gz)
sha256sums=('e212da6dc484ac26ec1ecb87f1f8351864f7c94030b8d386844f3de24f99c906')

package() {
  cd ${pkgname%-*}-$pkgver

  install -d "$pkgdir/usr/share/icons"
  cp -r ${pkgname%-*}{,-dark,-darker} "$pkgdir/usr/share/icons"

  install -Dm644 README "$pkgdir"/usr/share/doc/$pkgname/README
}
