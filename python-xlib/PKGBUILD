# Maintainer: hugo@barrera.io

pkgname=python-xlib
_gitname=python3-xlib
pkgver=0.15rc1
pkgrel=1
pkgdesc='Python 3 port of Xlib'
arch=(any)
url="https://github.com/LiuLang/python3-xlib"
license=('GPL2')
depends=('python')
source=("git+https://github.com/LiuLang/python3-xlib.git")
md5sums=('SKIP')


build() {
  cd "${srcdir}/${_gitname}"
  python setup.py build
  # make info
}

package() {
  cd "${srcdir}/${_gitname}"
  python setup.py install --root "$pkgdir"
}
