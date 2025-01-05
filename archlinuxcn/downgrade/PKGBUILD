# shellcheck disable=SC2034
# shellcheck disable=SC2154
# Author: Patrick Brisbin <pbrisbin@gmail.com>
pkgname=downgrade
pkgver=11.4.3
pkgrel=1
pkgdesc="Bash script for downgrading one or more packages to a version in your cache or the A.L.A."
arch=('any')
url="https://github.com/archlinux-downgrade/$pkgname"
license=('GPL')
backup=(etc/xdg/downgrade/downgrade.conf)
source=("downgrade-v$pkgver.tar.gz::https://github.com/archlinux-downgrade/$pkgname/archive/v$pkgver.tar.gz")
depends=('pacman-contrib' 'fzf') # pacsort
optdepends=('sudo: for installation via sudo')

package() {
  cd "$pkgname-$pkgver" || exit 1

  make DESTDIR="$pkgdir" PREFIX=/usr install
}
md5sums=('435aecca8d8cf9f9cfb137a940d6bed2')
