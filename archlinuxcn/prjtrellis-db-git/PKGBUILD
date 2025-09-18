# Maintainer:
# Contributor: Jan Samek <samekh@email.cz>

: ${_targets=ECP5 MachXO2}

_pkgname="prjtrellis-db"
pkgname="$_pkgname-git"
pkgver=r329.4dda149
pkgrel=2
pkgdesc='Project Trellis (Lattice ECP5 bit-stream format) database'
url="https://github.com/YosysHQ/prjtrellis-db"
license=('CC0-1.0')
arch=('any')

makedepends=('git')

_pkgsrc="$_pkgname"
source=("git+$url.git")
sha256sums=('SKIP')

provides=("$_pkgname=${pkgver%%\.*}")
conflicts=("$_pkgname")

pkgver() {
  cd "$_pkgsrc"
  printf 'r%s.%s' "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  cd "$_pkgsrc"

  install -dm 755 "$pkgdir"/usr/share/trellis/database
  cp -r --no-preserve=ownership devices.json $_targets "$pkgdir"/usr/share/trellis/database/

  install -Dm 644 COPYING -t "$pkgdir/usr/share/licenses/$pkgname/"
}
