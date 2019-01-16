_pkgname=sniffio
pkgname=python-sniffio
pkgver=1.0.0
pkgrel=2
pkgdesc="Sniff out which async library your code is running under"
arch=('any')
url="https://github.com/python-trio/sniffio"
license=('MIT')
depends=('python')
_name=${pkgname#python-}
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
md5sums=('f1ee89409cd401ca1bed64bb5945e495')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
