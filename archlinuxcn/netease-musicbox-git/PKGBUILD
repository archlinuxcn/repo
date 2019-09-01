# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Maintainer: Ariel AxionL <axionl@aosc.io>

pkgname=netease-musicbox-git
_gitname=musicbox
pkgver=r592.d09e2f0
pkgrel=1
pkgdesc="A sexy command line interface musicbox for NetEase based on Python"
arch=(any)
url="https://github.com/darknessomi/musicbox"
depends=('mpg123' 'python-pycryptodomex' 'python-requests' 'python-future' 'python-requests-cache')
makedepends=('python-setuptools' 'git')
optdepends=('aria2: music caching'
            'libnotify: notifications'
            'qt5-base: lyrics support'
            'python-pyqt5: lyrics support'
            'python-dbus: lyrics support')
provides=('netease-musicbox')
conflicts=('netease-musicbox')
install=${pkgname}.install
license=('MIT')

source=("${_gitname}::git+https://github.com/darknessomi/musicbox"
        "LICENSE::https://raw.githubusercontent.com/darknessomi/musicbox/master/LICENSE.txt"
        "0001-Replace_pyqt4_to_pyqt5_as_depends.patch")

sha256sums=('SKIP'
            'e6ce649439eace57267c94e651e38370582f883e6341b3203e951b9497433641'
            '485d7a1e900da50a4d6d055131ebc3b2072cf5760d9e27cd266ff373aedb6d46')

pkgver() {
  cd "${srcdir}/${_gitname}"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  cd "${srcdir}/${_gitname}"
  patch -Np1 -i "${srcdir}/0001-Replace_pyqt4_to_pyqt5_as_depends.patch"
}

package() {
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  cd "${srcdir}/${_gitname}"
  python setup.py install --root="${pkgdir}/" --optimize=1
  mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
