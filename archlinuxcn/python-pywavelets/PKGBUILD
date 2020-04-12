# Maintainer: Francois Boulogne <fboulogne at april dot org>
# Contributor: Jingbei Li <i@jingbei.li>
pkgname=python-pywavelets
_pkgname=pywt
pkgver=1.1.1
pkgrel=1
pkgdesc="Discrete Wavelet Transforms in Python"
arch=('x86_64' 'i686')
url="https://github.com/PyWavelets/pywt"
license=('MIT')
depends=('python' 'python-numpy')
makedepends=('python-setuptools' 'cython' 'python-numpy')
source=("https://github.com/PyWavelets/pywt/archive/v$pkgver.tar.gz")
sha256sums=('50fe2aae1b6d2462cf9e9b0dcc18dbcbd0b5ed65225abb4a272ed188dbcbceb0')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py build
}

package(){
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:ts=2:sw=2:et:
