# Contributor: Stefan Husmann <stefan-husmann@t-online.de>
# Maintainer: Steven Allen <steven@stebalien.com>

pkgname=stapler-git
pkgver=0.3.2.r11.gdc496c5
pkgrel=1
pkgdesc="Manipulate PDF documents from the command line"
url="http://github.com/hellerbarde/stapler"
arch=('any')
license=('BSD')
depends=('python2-pypdf2' 'python2-setuptools' 'python2-more_itertools')
makedepends=('git')
source=('git+https://github.com/hellerbarde/stapler.git')
md5sums=('SKIP')
_gitname="stapler"

pkgver() {
  cd "$srcdir/$_gitname"
  git describe --tags --always | sed -e 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd "$srcdir/$_gitname"
  sed -i '1s+python+python2+' stapler
  sed -i '1s+python+python2+' staplelib/tests.py
  sed -i '1s+python+python2+' staplelib/stapler.py
}

check() {
  cd "$srcdir/$_gitname"
  python2 setup.py test
}

package() {
  cd "$srcdir/$_gitname"
  python2 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1

  install -Dm644 LICENSE $pkgdir/usr/share/licenses/stapler-git/LICENSE
  install -Dm644 README.rst $pkgdir/usr/share/doc/stapler-git/README
}
