# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Maintainer: Ariel AxionL <axiionl@aosc.io>

pkgname=netease-musicbox
_gitname=musicbox
pkgver=0.2.5.2
pkgrel=1
pkgdesc="A sexy command line interface musicbox for NetEase based on Python"
arch=(any)
url="https://github.com/darknessomi/musicbox"
depends=('python' 'python-requests' 'python-setuptools' 'mpg123'
         'python-future' 'python-pycryptodomex' 'python-requests-cache')
optdepends=('aria2: music caching'
            'libnotify: notifications'
            'python-pyqt4: lyrics support'
            'python-dbus: lyrics support')
provides=('netease-musicbox')
conflicts=('netease-musicbox')
install=$pkgname.install
license=('MIT')

source=("musicbox-$pkgver.tar.gz::https://files.pythonhosted.org/packages/8e/54/17fb71a184020e2da960c4fbf1a0abf9fc8f774fa39a844ec47ef41ec4d9/NetEase-MusicBox-$pkgver.tar.gz"
        "LICENSE::https://raw.githubusercontent.com/darknessomi/musicbox/master/LICENSE.txt")

sha256sums=('017d452c2852d5f647e6917ad0d8a5e359fcc32e7ad34f6ea6db2c88d07d4086'
            '50efc98142cfffe413d73c87c91f2687dfb774217af923f03dfdc8426c9d9552')

package() {
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  cd "$srcdir/NetEase-MusicBox-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
  mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
