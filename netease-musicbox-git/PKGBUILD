# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Maintainer: Ariel AxionL <axionl@aosc.io>

pkgname=netease-musicbox-git
_gitname=musicbox
pkgver=r579.8ce4a7e
pkgrel=1
pkgdesc="A sexy command line interface musicbox for NetEase based on Python"
arch=(any)
url="https://github.com/darknessomi/musicbox"
depends=('mpg123' 'python-pycryptodomex' 'python-requests' 'python-future')
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
        "0001-Fixed-Replace_pyqt4_to_pyqt5_as_depends.patch")

sha256sums=('SKIP'
            '50efc98142cfffe413d73c87c91f2687dfb774217af923f03dfdc8426c9d9552'
            '55b4dd116b8b7a1b47854f52ce1e9f8422fb72702beb4c259bda388e23060484')

pkgver() {
  cd "${srcdir}/${_gitname}"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  cd "${srcdir}/${_gitname}"
  patch -Np1 -i "${srcdir}/0001-Fixed-Replace_pyqt4_to_pyqt5_as_depends.patch"
}

package() {
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  cd "${srcdir}/${_gitname}"
  python setup.py install --root="${pkgdir}/" --optimize=1
  mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
