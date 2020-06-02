_name=hstspreload
pkgname=python-hstspreload
pkgver=2020.6.2
pkgrel=1
pkgdesc="Chromium HSTS Preload list as a Python package and updated daily"
arch=(any)
url="https://github.com/sethmlarson/hstspreload"
license=('BSD-3')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/hstspreload-2020.6.2.tar.gz")
sha256sums=('5f9782b70f884eaaf2297872e73b8ada122d538bb7bdc41382a9fdfb2d61eb61')

build() {
  cd "$srcdir/hstspreload-2020.6.2"
  python3 setup.py build
}

package() {
  cd "$srcdir/hstspreload-2020.6.2"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

