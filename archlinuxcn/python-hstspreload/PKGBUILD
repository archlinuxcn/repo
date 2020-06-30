_name=hstspreload
pkgname=python-hstspreload
pkgver=2020.6.30
pkgrel=1
pkgdesc="Chromium HSTS Preload list as a Python package and updated daily"
arch=(any)
url="https://github.com/sethmlarson/hstspreload"
license=('BSD-3')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/hstspreload-2020.6.30.tar.gz")
sha256sums=('81225e82207ec316a774e5d130454327752853dfaf347b2bf4d21e524cc49efa')

build() {
  cd "$srcdir/hstspreload-2020.6.30"
  python3 setup.py build
}

package() {
  cd "$srcdir/hstspreload-2020.6.30"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

