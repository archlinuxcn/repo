_pkgname=libsass
pkgname=python-libsass
pkgver=0.14.5
pkgrel=1
pkgdesc="Sass for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="https://sass.github.io/libsass-python/"
license=('MIT')
depends=('python' 'python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
source=('https://files.pythonhosted.org/packages/2b/36/6bb1623bb6f8d218ac3a201b5366fb6505f30465ef9ef81a084432508d79/libsass-0.14.5.tar.gz')
md5sums=('86934693e4825b360594e88a734c3b72')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
