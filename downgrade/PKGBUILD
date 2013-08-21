# Author: Patrick Brisbin <pbrisbin@gmail.com>
pkgname=downgrade
pkgver=3.3
pkgrel=1
pkgdesc="Bash script for downgrading one or more packages to a version in your cache or the A.R.M."
arch=('any')
url="https://github.com/pbrisbin/downgrade"
license="GPL" 
source=($pkgname)
optdepends=('sudo: for installation via sudo')

package() {
  install -D -m755 $pkgname "$pkgdir/usr/bin/$pkgname"
}
md5sums=('7eb9b656fa6b72bb0b75b5f1ce539402')
