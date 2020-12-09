# Maintainer: Denton Liu <liu.denton@gmail.com>
#
# Credit to /u/ultimatt42:
# https://www.reddit.com/r/Stadia/comments/egcvpq/using_nintendo_switch_pro_controller_on_linux/fc5s7qm/

pkgname=nintendo-udev
pkgver=1.0.0
pkgrel=1
pkgdesc='udev rules for Nintendo Joy-Cons and Pro Controllers'
arch=('any')
license=('GPL')
source=('70-nintendo.rules')
sha256sums=('7b1f23f3134516c69612b38193ddd0ebda52467c1c1dcd306306323026697f97')

package() {
	cd "$srcdir"
	install -Dm644 70-nintendo.rules "$pkgdir"/usr/lib/udev/rules.d/70-nintendo.rules
}
