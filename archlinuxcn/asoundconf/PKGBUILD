# Maintainer: Lukas Jirkovsky <l.jirkovsky@gmail.com>
pkgname=asoundconf
pkgver=1.2
_pkgver=01a1f5320b0a
pkgrel=1
epoch=1
pkgdesc="Get and set configuration parameters in ~/.asoundrc.asoundconf"
arch=('any')
url="https://bitbucket.org/stativ/asoundconf"
license=('GPL')
depends=('python2')
optdepends=('pygtk: asoundconf-gtk GUI')
source=($pkgname-${pkgver}.tar.gz::https://bitbucket.org/stativ/asoundconf/get/${pkgver}.tar.gz)
md5sums=('aa12135497217f248e70c6aee286f453')

package() {
  cd "$srcdir/stativ-$pkgname-$_pkgver"
  python2 setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:
