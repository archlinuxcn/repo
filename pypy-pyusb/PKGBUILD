pkgbase=pypy3-pyusb
pkgname=(pypy3-pyusb pypy-pyusb)
pkgver=1.0.0b1
pkgrel=1
pkgdesc="A pure Python module which provides USB access."
arch=('any')
url="https://github.com/walac/pyusb"
license=('custom')
makedepends=('pypy3-setuptools' 'pypy-setuptools')
optdepends=('libusb-compat: for libusb0.1 backend'
  'libusb: for libusb1.0 backend')
source=("https://github.com/walac/pyusb/archive/${pkgver}.tar.gz")
md5sums=('fe439e0a84749f06eddd65927b7496ad')

build() {
  cp -a pyusb-$pkgver py2usb-$pkgver

  cd "$srcdir/pyusb-$pkgver"
  pypy3 setup.py build

  cd "$srcdir/py2usb-$pkgver"
  pypy setup.py build
}

package_pypy3-pyusb() {
  depends=('pypy3>=2.3' 'pypy3<2.4')
  cd "$srcdir/pyusb-$pkgver"

  pypy3 setup.py install --root="$pkgdir"
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

package_pypy-pyusb() {
  depends=('pypy')
  cd "$srcdir/py2usb-$pkgver"

  pypy setup.py install --root="$pkgdir"
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
