# Maintainer: Michael Lowman <michael.d.lowman@gmail.com>
pkgname=python2-netlib-git
_pyname=netlib
_gitname=netlib
pkgver=105.0ae37c7
pkgrel=1
pkgdesc='A collection of network utilities used by pathod and mitmproxy'
arch=('any')
url='https://github.com/cortesi/netlib'
license=('MIT')
depends=('python2')
makedepends=('git')
options=(!emptydirs)
provides=('python2-netlib')
conflicts=('python2-netlib')
source=("git://github.com/cortesi/${_gitname}.git")
md5sums=('SKIP')

package() {
  cd "${srcdir}/${_gitname}"
  python2 setup.py install --root="${pkgdir}/" --optimize=1
}

pkgver() {
  cd "${srcdir}/${_gitname}"
  echo $(git rev-list --count master).$(git rev-parse --short master)
}
