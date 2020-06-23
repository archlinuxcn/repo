_name=hstspreload
pkgname=python-hstspreload
pkgver=2020.6.23
pkgrel=1
pkgdesc="Chromium HSTS Preload list as a Python package and updated daily"
arch=(any)
url="https://github.com/sethmlarson/hstspreload"
license=('BSD-3')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/hstspreload-2020.6.23.tar.gz")
sha256sums=('4c55cb73ebe3549277a4e5e5a95867350cd3888ebe09d41f61a42718e4a3909e')

build() {
  cd "$srcdir/hstspreload-2020.6.23"
  python3 setup.py build
}

package() {
  cd "$srcdir/hstspreload-2020.6.23"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

