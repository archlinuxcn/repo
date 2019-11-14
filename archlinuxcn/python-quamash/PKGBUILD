# Maintainer: Bruce Zhang <zttt183525594@gmail.com>
pkgname=python-quamash
_pkgname=Quamash
pkgver=0.6.1
pkgrel=7
pkgdesc="Implementation of the asyncio (PEP 3156) event-loop with Qt"
arch=('any')
url="https://github.com/harvimt/quamash"
license=('BSD')
depends=('python')
makedepends=('python-setuptools' 'icu' 'python-pyqt5' 'qt5-base')
optdepends=(
  'python-pyqt5: PyQt5 implementation' 
  'python-pyside: PySide implementation'
)
source=(
  "https://files.pythonhosted.org/packages/01/1e/cf6f3c38cee61ed04fea58667f673adc67d6412eba0b3327dbb5732c1177/$_pkgname-$pkgver.tar.gz" 
  "LICENSE::https://raw.githubusercontent.com/harvimt/quamash/master/LICENSE"
)
sha256sums=('6a31a6c9be7c20591e65a082b87566c82ccdfee4a7a11714655bd41b98f61b5c'
            '516399e35b13515ae36d61e195f55a9b28288636c29d4e3a5f62b54cef3e8653')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
  install -Dm644 "$srcdir"/LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
