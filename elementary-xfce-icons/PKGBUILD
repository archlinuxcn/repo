# Maintainer: Hugo Osvaldo Barrera <hugo@barrera.io>
# Contributor: Limao Luo <luolimao+AUR@gmail.com>
# Contributor: flan_suse <windows2linux@zoho.com>
# Contributor: auscompgeek <auscompgeek@zoho.com>

pkgname=elementary-xfce-icons
_pkgname=elementary-xfce
pkgver=0.7
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
source=($pkgname-$pkgver.tar.gz::https://github.com/shimmerproject/${pkgname%-*}/archive/$pkgver.tar.gz)
sha256sums=('df13a02929cf7235582b511d9014afc05771b72bcb345cc366e91c2dec89a0b8')

package() {
  cd ${pkgname%-*}-$pkgver

  install -d "$pkgdir/usr/share/icons"
  cp -r ${_pkgname}{,-dark,-darker} "$pkgdir/usr/share/icons"

  install -Dm644 README "$pkgdir"/usr/share/doc/$pkgname/README
}
