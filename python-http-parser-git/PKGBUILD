# Maintainer: lilydjwg <lilydjwg@gmail.com>
pkgname=python-http-parser-git
pkgver=0.8.3
epoch=1
pkgrel=1
pkgdesc="HTTP request/response parser for python in C"
arch=('x86_64' 'i686')
url="https://github.com/benoitc/http-parser"
license=('BSD')
depends=('python')
makedepends=('git' 'python-setuptools')
md5sums=(SKIP)
_gitroot="git://github.com/benoitc/http-parser.git"
_gitname="http-parser"
source=($_gitroot)

pkgver() {
  cd "$srcdir/$_gitname"
  git describe --tags | sed 's/-/./;s/-/_/g'
}

package() {
  cd "$srcdir/$_gitname"
  python3 setup.py install --root="$pkgdir/" --optimize=1
}

