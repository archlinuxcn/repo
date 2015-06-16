# Maintainer: Jiachen Yang <farseerfc@gmail.com>
pkgname=netease-musicbox
_gitname=musicbox
pkgver=r140.31ff39b
pkgrel=1
pkgdesc="A sexy command line interface musicbox for NetEase based on Python"
arch=(any)
url="https://github.com/darknessomi/musicbox"
license=('MIT')
depends=('python2' 'mpg123' 'python2-beautifulsoup4' 'python2-requests' 'python2-setuptools')
makedepends=('git')
options=(!emptydirs)
source=("git+https://github.com/darknessomi/musicbox")
sha256sums=('SKIP')
install=$pkgname.install

pkgver() {
  cd $_gitname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  cd "$srcdir/$_gitname"
  python2 setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:
