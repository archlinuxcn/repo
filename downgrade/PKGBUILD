# Author: Patrick Brisbin <pbrisbin@gmail.com>
pkgname=downgrade
pkgver=5.3.0
pkgrel=1
pkgdesc="Bash script for downgrading one or more packages to a version in your cache or the A.R.M."
arch=('any')
url="https://github.com/pbrisbin/$pkgname"
license=('GPL')
source=("https://github.com/pbrisbin/$pkgname/archive/v$pkgver.tar.gz")
optdepends=('sudo: for installation via sudo')

package() {
  local po_file

  cd "$pkgname-$pkgver"

  for po_file in locale/*.po; do
    locale="$(basename "$po_file" .po)"

    mkdir -p "$pkgdir/usr/share/locale/$locale/LC_MESSAGES/"
    msgfmt "$po_file" -o "$pkgdir/usr/share/locale/$locale/LC_MESSAGES/$pkgname.mo"
  done

  make PREFIX=/usr DESTDIR="$pkgdir" install
}
md5sums=('c5d5cca7d47a1ea01a3d59205a2a0feb')
