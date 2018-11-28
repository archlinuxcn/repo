# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Maintainer: Ariel AxionL <axiionl@aosc.io>

pkgname=netease-musicbox
_gitname=musicbox
pkgver=0.2.5.4
pkgrel=1
pkgdesc="A sexy command line interface musicbox for NetEase based on Python"
arch=(any)
url="https://github.com/darknessomi/musicbox"
depends=('mpg123' 'python-pycryptodomex' 'python-requests' 'python-future')
makedepends=('python-setuptools')
optdepends=('aria2: music caching'
            'libnotify: notifications'
            'qt5-base: lyrics support'
            'python-pyqt5: lyrics support'
            'python-dbus: lyrics support')
provides=('netease-musicbox')
conflicts=('netease-musicbox')
install=$pkgname.install
license=('MIT')

source=("musicbox-$pkgver.tar.gz::https://github.com/darknessomi/musicbox/archive/0.2.5.4.tar.gz"
        "LICENSE::https://raw.githubusercontent.com/darknessomi/musicbox/master/LICENSE.txt"
        "0001Replace_pyqt4_to_pyqt5_as_depends.patch"
        "0002Remove_python_requests_cache_as_depends.patch")     

sha256sums=('4fdfd9061dfdec181736b56166a11bfe27ae9c4011f9c266b57fdfbca232afa3'
            '50efc98142cfffe413d73c87c91f2687dfb774217af923f03dfdc8426c9d9552'
            'c910c12c5ffe23b3cc582fb718017c8dee5ef4e9dacfb1944f35266a79f8bbee'
            '24b74424cd624742e35631fafd24ad6fd6527807728deeb1cc0a81a1415370b7')

prepare() {
  cd "${srcdir}/musicbox-${pkgver}"
  patch -Np1 -i "${srcdir}/0001Replace_pyqt4_to_pyqt5_as_depends.patch"
  patch -Np1 -i "${srcdir}/0002Remove_python_requests_cache_as_depends.patch"
}

package() {
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  cd "${srcdir}/musicbox-${pkgver}"
  python setup.py install --root="${pkgdir}/" --optimize=1
}
# vim:set ts=2 sw=2 et:
