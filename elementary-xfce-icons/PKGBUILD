# Maintainer: mortzprk <mortz.prk@gmail.com>
# Contributor: Hugo Osvaldo Barrera <hugo@barrera.io>
# Contributor: Limao Luo <luolimao+AUR@gmail.com>
# Contributor: flan_suse <windows2linux@zoho.com>
# Contributor: auscompgeek <auscompgeek@zoho.com>

pkgname=elementary-xfce-icons
pkgver=0.8
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
sha256sums=('15f08395b89e955f479faf9bc9eaab7bc56f4d4f7d365a38b4b282a443a79c1a')

package() {
  cd ${pkgname%-*}-$pkgver

  install -d "$pkgdir/usr/share/icons"
  cp -r ${pkgname%-*}{,-dark,-darker} "$pkgdir/usr/share/icons"

  install -Dm644 README "$pkgdir"/usr/share/doc/$pkgname/README
}
