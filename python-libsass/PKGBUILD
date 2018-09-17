_pkgname=libsass
pkgname=python-libsass
pkgver=0.15.0
pkgrel=1
pkgdesc="Sass for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="https://sass.github.io/libsass-python/"
license=('MIT')
depends=('python' 'python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
source=('https://files.pythonhosted.org/packages/00/e4/28f7fc87da16f2d0a982a01856b10bff2bc52d87b850fdf86196ebade4f9/libsass-0.15.0.tar.gz')
md5sums=('9343d3b34afe8d5b36cc49c4535ff00d')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
