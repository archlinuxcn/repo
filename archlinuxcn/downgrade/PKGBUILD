# shellcheck disable=SC2034
# shellcheck disable=SC2154
# Author: Patrick Brisbin <pbrisbin@gmail.com>
pkgname=downgrade
pkgver=6.1.0
pkgrel=0
pkgdesc="Bash script for downgrading one or more packages to a version in your cache or the A.L.A."
arch=('any')
url="https://github.com/pbrisbin/$pkgname"
license=('GPL')
source=("https://github.com/pbrisbin/$pkgname/archive/v$pkgver.tar.gz")
depends=('pacman-contrib') # pacsort
optdepends=('sudo: for installation via sudo')

package() {
  local po_file

  cd "$pkgname-$pkgver" || exit 1

  for po_file in locale/*.po; do
    locale="$(basename "$po_file" .po)"

    mkdir -p "$pkgdir/usr/share/locale/$locale/LC_MESSAGES/"
    msgfmt "$po_file" -o "$pkgdir/usr/share/locale/$locale/LC_MESSAGES/$pkgname.mo"
  done

  make PREFIX=/usr DESTDIR="$pkgdir" install
}
md5sums=('8ba498cdae1e3185b48db05f754608a3')
