# Author: Patrick Brisbin <pbrisbin@gmail.com>
pkgname=downgrade
pkgver=4.2
pkgrel=1
pkgdesc="Bash script for downgrading one or more packages to a version in your cache or the A.R.M."
arch=('any')
url="https://github.com/pbrisbin/downgrade"
license="GPL" 
source=($pkgname lt.po nb.po nn.po)
optdepends=('sudo: for installation via sudo')

package() {
  local locales="lt nb nn" # space separated

  for i in $locales; do
    mkdir -p "$pkgdir/usr/share/locale/$i/LC_MESSAGES/"
    msgfmt "$srcdir/$i.po" -o "$pkgdir/usr/share/locale/$i/LC_MESSAGES/downgrade.mo"
  done

  install -D -m755 $pkgname "$pkgdir/usr/bin/$pkgname"
}
md5sums=('bc7f8aea1becb16c3ded2535724b9370'
         '06a79a5c7a033689afa7d3fa3a7160b0'
         '75a4b3e892cc91d9d256e5fadea34382'
         'cdffd10b833014d945f1542a9e706dd5')
