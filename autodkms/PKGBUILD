# Maintainer: phoenixlzx <phoenixlzx at archlinuxcn.org>

pkgname=autodkms
pkgver=0.1
pkgrel=1
pkgdesc="mkinitcpio hook to compile all dkms modules"
url=("https://github.com/phoenixlzx/autodkms")
arch=('any')
license=('MIT')
depends=('dkms')
install=autodkms.install
source=("https://raw.github.com/phoenixlzx/autodkms/master/autodkms")
sha256sums=("f2256cc3ef2db4b284f73ce0ed2d2a591d82a4f2b9ee112da12cff8eb27f89a1")

package() {
  cd "${srcdir}"
  install -dm 755 "${pkgdir}"/usr/lib/initcpio/install
  install -m 644 autodkms "${pkgdir}"/usr/lib/initcpio/install/autodkms
}
