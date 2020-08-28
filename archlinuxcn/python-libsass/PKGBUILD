_name=libsass
pkgname=python-libsass
pkgver=0.20.1
pkgrel=1
pkgdesc="Sass for Python: A straightforward binding of libsass for Python."
arch=('x86_64')
url="https://sass.github.io/libsass-python/"
license=('MIT License')
depends=('python-six' 'libsass' 'python-setuptools')
makedepends=('gcc')
provides=('sassc')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/libsass-0.20.1.tar.gz")
sha256sums=('e0e60836eccbf2d9e24ec978a805cd6642fa92515fbd95e3493fee276af76f8a')

build() {
  cd "$srcdir/libsass-0.20.1"
  python3 setup.py build
}

package() {
  cd "$srcdir/libsass-0.20.1"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

