# Maintainer: Stephen Zhang <zsrkmyn at gmail dot com>
# Co-maintainer: Jiachen Yang <farseerfc@gmail.com>
# Co-maintainer: lilydjwg <lilydjwg@gmail.com>

pkgname=nvchecker-git
pkgver=0.5dev.4
pkgrel=1
pkgdesc="a tool for checking if a new version of some software has been released."
arch=('any')
url="https://github.com/lilydjwg/nvchecker"
license=('MIT')
depends=('python' 'python-setuptools')
makedepends=('git')
optdepends=('python-aiohttp: HTTP client (only one needed)'
            'python-tornado: HTTP client (only one needed)'
            'python-pycurl: better HTTP support for Tornado'
            'git'
            'mercurial')
source=('git://github.com/lilydjwg/nvchecker.git')
md5sums=('SKIP')

_gitroot=nvchecker

pkgver() {
  cd "$srcdir/$_gitroot"
  echo $(awk '$1 == "__version__" { gsub(/\x27/, "", $3); print $3 }' nvchecker/__init__.py).$(git describe --long | cut -d. -f2)
}

build() {
  cd $srcdir/$_gitroot
  python3 setup.py build
}

package() {
  cd $srcdir/$_gitroot
  python3 setup.py install --root="$pkgdir" --optimize=1 --skip-build
}

# vim:set ts=2 sw=2 et:
