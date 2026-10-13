# shellcheck disable=SC2034
# shellcheck disable=SC2154
# Author: Patrick Brisbin <pbrisbin@gmail.com>
pkgname=downgrade
pkgver=12.0.4
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
sha256sums=('6049701f233ecbc39a1b0b4c7921c1433dda12a1545b55f6264f60867abf84ba')
