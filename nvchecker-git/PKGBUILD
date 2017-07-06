# Maintainer: Stephen Zhang <zsrkmyn at gmail dot com>
# Co-maintainer: Jiachen Yang <farseerfc@gmail.com>
# Co-maintainer: lilydjwg <lilydjwg@gmail.com>

pkgname=nvchecker-git
pkgver=v0.4.4.r16.ga82c18c
pkgrel=1
pkgdesc="a tool for checking if a new version of some software has been released."
arch=('any')
url="https://github.com/lilydjwg/nvchecker"
license=('MIT')
depends=('python' 'python-aiohttp' 'python-setuptools')
makedepends=('git')
optdepends=('git' 'mercurial')
source=('git://github.com/lilydjwg/nvchecker.git')
md5sums=('SKIP')

_gitroot=nvchecker

pkgver() {
  cd "$srcdir/$_gitroot"
  git describe --long | sed -r 's/([^-]*-g)/r\1/;s/-/./g'
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
