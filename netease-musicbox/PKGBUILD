# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Maintainer: Ariel AxionL <axiionl@aosc.io>

pkgname=netease-musicbox
_gitname=musicbox
pkgver=0.2.4.3
pkgrel=1
pkgdesc="A sexy command line interface musicbox for NetEase based on Python"
arch=(any)
url="https://github.com/darknessomi/musicbox"
depends=('mpg123' 'python' 'python-crypto' 'python-cryptography')
makedepends=('python-beautifulsoup4' 
             'python-requests' 'python-setuptools' 
             'python-future' 'python-lxml')
optdepends=('aria2: music caching'
            'libnotify: notifications'
            'python-pyqt4: lyrics support'
            'python-dbus: lyrics support')
provides=('netease-musicbox')
conflicts=('netease-musicbox')
install=$pkgname.install
license=('MIT')

source=("musicbox-$pkgver.tar.gz::https://github.com/darknessomi/musicbox/archive/$pkgver.tar.gz")

sha256sums=('9ff9403d06f7fa714269d6c46beba6236861c9f639391a88f87a2eb3f6bf2ebb')

package() {
  cd "$srcdir/$_gitname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
  mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m755 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/"
}
# vim:set ts=2 sw=2 et: