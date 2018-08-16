# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Maintainer: Ariel AxionL <axiionl@aosc.io>

pkgname=netease-musicbox
_gitname=musicbox
pkgver=0.2.5.3
pkgrel=1
pkgdesc="A sexy command line interface musicbox for NetEase based on Python"
arch=(any)
url="https://github.com/darknessomi/musicbox"
depends=('mpg123' 'python-pycryptodomex' 'python-requests')
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

source=("musicbox-$pkgver.tar.gz::https://files.pythonhosted.org/packages/12/63/d65c908d4e76ad04622597f5d6e1f5742bc50fbd12e20f80a23736d533fe/NetEase-MusicBox-$pkgver.tar.gz"
        "LICENSE::https://raw.githubusercontent.com/darknessomi/musicbox/master/LICENSE.txt"
        "0001Remove_python_requests_cache_as_depends.patch"
        "0002Replace_pyqt4_to_pyqt5_as_depends.patch")

sha256sums=('1688d8ff1898bc4a0b785187d122eed47c61a1ec017cf07d95139692dd0ea008'
            '50efc98142cfffe413d73c87c91f2687dfb774217af923f03dfdc8426c9d9552'
            '85c4bd50059c6f038bcb1add01d67ecdb4f87d2861a30bcbe0ef97b8ee5172a2'
            '0d1a68ccb2c588753a1548775ae7a94de39f33d54744bde507a3bf9532039b0c')

prepare() {
  cd "${srcdir}/NetEase-MusicBox-${pkgver}"
  patch -Np1 -i "${srcdir}/0001Remove_python_requests_cache_as_depends.patch"
  patch -Np1 -i "${srcdir}/0002Replace_pyqt4_to_pyqt5_as_depends.patch"
}

package() {
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  cd "${srcdir}/NetEase-MusicBox-${pkgver}"
  python setup.py install --root="${pkgdir}/" --optimize=1
  mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
