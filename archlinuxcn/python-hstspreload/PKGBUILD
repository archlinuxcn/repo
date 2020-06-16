_name=hstspreload
pkgname=python-hstspreload
pkgver=2020.6.16
pkgrel=1
pkgdesc="Chromium HSTS Preload list as a Python package and updated daily"
arch=(any)
url="https://github.com/sethmlarson/hstspreload"
license=('BSD-3')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/hstspreload-2020.6.16.tar.gz")
sha256sums=('06a634aa0be9a51560be8dccfeceddeba6a2f0a9273433d778c93cdaf93c86d0')

build() {
  cd "$srcdir/hstspreload-2020.6.16"
  python3 setup.py build
}

package() {
  cd "$srcdir/hstspreload-2020.6.16"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

