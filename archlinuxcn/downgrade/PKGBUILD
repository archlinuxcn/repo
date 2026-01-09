# shellcheck disable=SC2034
# shellcheck disable=SC2154
# Author: Patrick Brisbin <pbrisbin@gmail.com>
pkgname=downgrade
pkgver=11.8.0
pkgrel=1
pkgdesc="Bash script for downgrading one or more packages to a version in your cache or the A.L.A."
arch=('any')
url="https://github.com/archlinux-downgrade/$pkgname"
license=('GPL')
backup=(etc/xdg/downgrade/downgrade.conf)
source=("https://github.com/archlinux-downgrade/$pkgname/releases/download/v${pkgver//_/-}/downgrade-${pkgver//_/-}.tar.gz")
depends=('pacman-contrib' 'fzf') # pacsort
optdepends=('sudo: for installation via sudo')

package() {
  cd "$pkgname-${pkgver//_/-}" || exit 1

  make DESTDIR="$pkgdir" PREFIX=/usr install
}
md5sums=('14191f5c3326c37ff4e2aaeef55c82d1')
