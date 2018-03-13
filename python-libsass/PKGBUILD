_pkgname=libsass
pkgname=python-libsass
pkgver=0.14.1
pkgrel=1
pkgdesc="Sass for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="https://sass.github.io/libsass-python/"
license=('MIT')
depends=('python' 'python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
source=('https://pypi.python.org/packages/bb/8b/1214ee4ff18b6a490a963e80df3b835e5bc2e94130d817ee4f37ec130ac6/libsass-0.14.1.tar.gz')
md5sums=('672ea2231a51560667542c14fea48225')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
