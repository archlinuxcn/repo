# shellcheck disable=SC2034
# shellcheck disable=SC2154
# Author: Patrick Brisbin <pbrisbin@gmail.com>
pkgname=downgrade
pkgver=10.1.0
pkgrel=1
pkgdesc="Bash script for downgrading one or more packages to a version in your cache or the A.L.A."
arch=('any')
url="https://github.com/pbrisbin/$pkgname"
license=('GPL')
backup=(etc/xdg/downgrade/downgrade.conf)
source=("downgrade-v$pkgver.tar.gz::https://github.com/pbrisbin/$pkgname/archive/v$pkgver.tar.gz")
depends=('pacman-contrib') # pacsort
optdepends=('sudo: for installation via sudo')

package() {
  cd "$pkgname-$pkgver" || exit 1

  make DESTDIR="$pkgdir" PREFIX=/usr install
}
md5sums=('7c01fe20de7ef953f0143884b707054f')
