# Maintainer: mutantmonkey <aur@mutantmonkey.in>
pkgname=python2-pyptlib
_pkgname=pyptlib
pkgver=0.0.6
pkgrel=1
pkgdesc="A python implementation of the Pluggable Transports for Circumvention specification for Tor"
arch=('any')
url="https://pypi.python.org/pypi/pyptlib"
license=('BSD')
depends=('python2')
source=("https://pypi.python.org/packages/source/p/pyptlib/pyptlib-${pkgver}.tar.gz"
        "https://pypi.python.org/packages/source/p/pyptlib/pyptlib-${pkgver}.tar.gz.asc")
sha256sums=('b98472e3d9e8f4689d3913ca8f89afa5e6cc5383dcd8686987606166f9dac607'
            'SKIP')

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python2 setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:
