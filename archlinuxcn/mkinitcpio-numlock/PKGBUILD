# Maintainer: Matej Groma <sbovdvvnir68a8hftegth9whs+arch-aur@matejgroma.com>
# Contributor: Jordi De Groof <jordi.degroof@gmail.com>

pkgname=mkinitcpio-numlock
pkgver=1.0.3
pkgrel=1
pkgdesc="Enable numlock in early userspace"
arch=('any')
url="https://bbs.archlinux.org/viewtopic.php?pid=869618"
license=('GPL')
depends=('mkinitcpio' 'kbd')
source=(numlock_hook numlock_install)
sha512sums=('f623a8e6b015b9a798c4bec2ec90c2638b6c966e82be8910601cdaabe3660f05d3ca3e531d2a8ba747b053631f073a6e90c4eb2c9c04f39b84b7f7c8014696ea'
            '65f21cbe70e11df366779fdd135c662fbc4cc1511d527294f7af590fa5d6a9004d6d9f9e706560dfe1a859088e85850c98a8431881da91d560002a3ce7ef114f')

package() {
  install -o root -g root -m 644 -D ${srcdir}/numlock_hook ${pkgdir}/usr/lib/initcpio/hooks/numlock
  install -o root -g root -m 644 -D ${srcdir}/numlock_install ${pkgdir}/usr/lib/initcpio/install/numlock
}
