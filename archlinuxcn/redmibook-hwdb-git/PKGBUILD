# Maintainer: oldherl <oldherl@gmail.com>

pkgname=redmibook-hwdb-git
_pkgname=redmibook-hwdb
pkgver=0.0.r2.gc050119
pkgrel=1
pkgdesc="hwdb rules for my RedmiBook Pro laptop"
url="https://github.com/oldherl/redmibook-hwdb"
license=("custom:MIT")
arch=(any)
source=("git+https://github.com/oldherl/redmibook-hwdb.git")
sha256sums=('SKIP')
makedepends=('git')
depends=('systemd')

pkgver() {
  cd "$srcdir/$_pkgname"
  git describe --tags --always | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}
package(){
  cd "$srcdir/$_pkgname"
  install -d "$pkgdir/usr/lib/udev/hwdb.d"
  install -m644 *.hwdb "$pkgdir/usr/lib/udev/hwdb.d/"
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/${_pkgname}/LICENSE"
} 

