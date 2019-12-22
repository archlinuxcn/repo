# Maintainer: fzerorubigd <fzero@rubi.gd>
_pkgmain=pgspecial
pkgname=python-$_pkgmain
pkgver=1.11.9
pkgrel=2
pkgdesc="Meta-commands handler for Postgres Database."
arch=('any')
url="https://github.com/dbcli/pgspecial"
license=('BSD')
groups=()
depends=('python')
provides=('python-pgspecial')
makedepends=('python-setuptools')
options=(!emptydirs)
source=($pkgname-$pkgver.zip::https://github.com/dbcli/pgspecial/archive/v${pkgver}.zip)

package() {
  cd "$srcdir/$_pkgmain-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}
md5sums=('69def4a0d8776a89813c2b6a64e58eb1')
