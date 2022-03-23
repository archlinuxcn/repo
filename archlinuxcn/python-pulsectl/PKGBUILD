# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: WorMzy Tykashi <wormzy.tykashi@gmail.com>
pkgname=python-pulsectl
_name=${pkgname#python-}
pkgver=22.3.2
pkgrel=1
epoch=1
pkgdesc="Python high-level interface and ctypes-based bindings for PulseAudio (libpulse)"
arch=('any')
url="https://github.com/mk-fg/python-pulse-control"
license=('MIT')
depends=('python' 'libpulse')
makedepends=('python-setuptools')
conflicts=('python-pulse-control')
replaces=('python-pulse-control')
changelog="$_name-CHANGES.rst"
source=("https://pypi.org/packages/source/${_name:0:1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('cc174e1ceebd4e6222c5b78f4f415f12e80753c9ab75ab354159b4cb5950b084')

build() {
  cd "$_name-$pkgver"
  python setup.py build
}

package() {
  cd "$_name-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build

  install -Dm644 COPYING -t "$pkgdir/usr/share/licenses/$pkgname"
}
