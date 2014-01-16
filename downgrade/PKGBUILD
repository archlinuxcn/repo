# Author: Patrick Brisbin <pbrisbin@gmail.com>
pkgname=downgrade
pkgver=5.0.3
pkgrel=1
pkgdesc="Bash script for downgrading one or more packages to a version in your cache or the A.R.M."
arch=('any')
url="https://github.com/pbrisbin/$pkgname"
license="GPL" 
source=(
  $pkgname
  ${pkgname}.8
  bash_completion
  zsh_completion
  fr.po
  lt.po
  nb.po
  nn.po
)
optdepends=('sudo: for installation via sudo')

package() {
  local po_file

  for po_file in *.po; do
    locale="${po_file%.po}"

    mkdir -p "$pkgdir/usr/share/locale/$locale/LC_MESSAGES/"
    msgfmt "$po_file" -o "$pkgdir/usr/share/locale/$locale/LC_MESSAGES/$pkgname"
  done

  install -Dm755 $pkgname        "$pkgdir/usr/bin/$pkgname"
  install -Dm644 ${pkgname}.8    "$pkgdir/usr/share/man/man8/${pkgname}.8"
  install -Dm644 bash_completion "$pkgdir/etc/bash_completion.d/downgrade"
  install -Dm644 zsh_completion  "$pkgdir/usr/share/zsh/site-functions/_downgrade"
}
md5sums=('53356fda6ea666334ea2b207df99b027'
         'bce61c026931ea4b9c99e3cbc7ef9c1c'
         '38c8fc5c15d36252cb703f568d5a4544'
         '7dfcbe3c86f264e0cb2f3ad24be6e082'
         '49e286b0064071356aa7791d2530bebf'
         'd3818b3b5d85f83e425d8d1c614fdfa2'
         '31beb2bd6ca7ed713eb5601ba3147f77'
         '6a7723c9634d39d25a8f29483995d40b')
