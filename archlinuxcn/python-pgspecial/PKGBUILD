# Maintainer: fzerorubigd <fzero@rubi.gd>
_pkgmain=pgspecial
pkgname=python-$_pkgmain
pkgver=1.11.5
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
md5sums=('9d1b56f349124405a42d6ffe5461b097')
