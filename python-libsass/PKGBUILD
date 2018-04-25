_pkgname=libsass
pkgname=python-libsass
pkgver=0.14.4
pkgrel=1
pkgdesc="Sass for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="https://sass.github.io/libsass-python/"
license=('MIT')
depends=('python' 'python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
source=('https://files.pythonhosted.org/packages/cf/f1/97b4f914c85380f65b235e5db956db1279aaf1943e1cbd5dd05e8c871b6f/libsass-0.14.4.tar.gz')
md5sums=('b10f81c8e3ca301aa26909486bfd0f4d')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
}

# vim:set sw=2 et:
