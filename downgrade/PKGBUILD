# Author: Patrick Brisbin <pbrisbin@gmail.com>
pkgname=downgrade
pkgver=5.1
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
  zh_CN.po
)
optdepends=('sudo: for installation via sudo')

package() {
  local po_file

  for po_file in *.po; do
    locale="${po_file%.po}"

    mkdir -p "$pkgdir/usr/share/locale/$locale/LC_MESSAGES/"
    msgfmt "$po_file" -o "$pkgdir/usr/share/locale/$locale/LC_MESSAGES/$pkgname.mo"
  done

  install -Dm755 $pkgname        "$pkgdir/usr/bin/$pkgname"
  install -Dm644 ${pkgname}.8    "$pkgdir/usr/share/man/man8/${pkgname}.8"
  install -Dm644 bash_completion "$pkgdir/etc/bash_completion.d/downgrade"
  install -Dm644 zsh_completion  "$pkgdir/usr/share/zsh/site-functions/_downgrade"
}
md5sums=('e4b6a5a5dde5eac338422451103384ce'
         '22999424811e44ef287eedb47fd16e27'
         '38c8fc5c15d36252cb703f568d5a4544'
         '7dfcbe3c86f264e0cb2f3ad24be6e082'
         '1cc22667d0af7af8483d85a1586a3a75'
         'c7b50dde7b06c90dc728f56d374ab22a'
         'e1f7859463ca1d023a85f3fca5a44454'
         '0f4ce1ee531eb309c6e31b4153fe4a92'
         'dd61159825cadb14063998ef3e9b120f')
