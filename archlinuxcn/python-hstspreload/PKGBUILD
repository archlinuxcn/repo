_name=hstspreload
pkgname=python-hstspreload
pkgver=2020.5.13
pkgrel=1
pkgdesc="Chromium HSTS Preload list as a Python package and updated daily"
arch=(any)
url="https://github.com/sethmlarson/hstspreload"
license=('BSD-3')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('0cad9cfe67d461444b63a504afcde7be303741d57e3039295ec25db10d0c102a')

build() {
  cd "$srcdir/$_name-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_name-$pkgver"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

