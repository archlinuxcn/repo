# Contributor: Stefan Husmann <stefan-husmann@t-online.de>
# Maintainer: Steven Allen <steven@stebalien.com>

pkgname=stapler-git
pkgver=1.0.0
pkgrel=1
pkgdesc="Manipulate PDF documents from the command line"
url="http://github.com/hellerbarde/stapler"
arch=('any')
license=('BSD')
depends=('python-pypdf2' 'python-more-itertools')
makedepends=('git' 'python-pip')
source=('git+https://github.com/hellerbarde/stapler.git')
md5sums=('SKIP')
_gitname="stapler"

pkgver() {
  cd "$srcdir/$_gitname"
  git describe --tags --always | sed -e 's/\([^-]*-g\)/r\1/;s/-/./g'
}

package() {
  cd "$srcdir/$_gitname"
  pip install --no-deps \
      --no-warn-script-location \
      --root="$pkgdir" --isolated \
      --compile -I .
  rm "$pkgdir/usr/bin/pdf-stapler" # Same as stapler.

  install -Dm644 LICENSE $pkgdir/usr/share/licenses/stapler-git/LICENSE
  install -Dm644 README.rst $pkgdir/usr/share/doc/stapler-git/README
}
