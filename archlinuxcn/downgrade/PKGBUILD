# shellcheck disable=SC2034
# shellcheck disable=SC2154
# Author: Patrick Brisbin <pbrisbin@gmail.com>
pkgname=downgrade
pkgver=6.2.5
pkgrel=1
pkgdesc="Bash script for downgrading one or more packages to a version in your cache or the A.L.A."
arch=('any')
url="https://github.com/pbrisbin/$pkgname"
license=('GPL')
source=("downgrade-v$pkgver.tar.gz::https://github.com/pbrisbin/$pkgname/archive/v$pkgver.tar.gz")
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
md5sums=('97bb4820e09d16e2eb045f4a77b9a3be')
