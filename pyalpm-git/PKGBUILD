# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: Dave Reisner <d@falconindy.com>

_pkgname=pyalpm
pkgname=$_pkgname-git
pkgver=0.8.4.r8.g06fa0ea
pkgrel=1
pkgdesc="Libalpm bindings for Python 3 (Git version)"
arch=('x86_64')
url="https://git.archlinux.org/pyalpm.git/"
license=('GPL3')
depends=('python>=3.6' 'pacman>=5')
makedepends=('git')
checkdepends=('python-nose')
provides=("$_pkgname=$pkgver")
conflicts=("$_pkgname")
source=('git+https://git.archlinux.org/pyalpm.git')
sha256sums=('SKIP')

pkgver() {
  cd $_pkgname
  ( set -o pipefail
    git describe --long --tags 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
  )
}

build() {
  cd $_pkgname

  python setup.py build
}

check() {
  cd $_pkgname

  PYTHONPATH="$(ls -d build/lib.linux-$CARCH-*)" nosetests -v tests
}

package() {
  cd $_pkgname

  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
