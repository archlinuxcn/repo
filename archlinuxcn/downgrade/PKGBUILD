# shellcheck disable=SC2034
# shellcheck disable=SC2154
# Author: Patrick Brisbin <pbrisbin@gmail.com>
pkgname=downgrade
pkgver=12.0.1
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
sha256sums=('4f445339e2465907d3d3a3c143088b9ffd39dcde152a13d7892f464bc649073f')
