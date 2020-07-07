_name=hstspreload
pkgname=python-hstspreload
pkgver=2020.7.7
pkgrel=1
pkgdesc="Chromium HSTS Preload list as a Python package and updated daily"
arch=(any)
url="https://github.com/sethmlarson/hstspreload"
license=('BSD-3')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/hstspreload-2020.7.7.tar.gz")
sha256sums=('3e1b107d6c865fc28f0f023456f193f2e916d14bca5a16c93fe440bef90c7c58')

build() {
  cd "$srcdir/hstspreload-2020.7.7"
  python3 setup.py build
}

package() {
  cd "$srcdir/hstspreload-2020.7.7"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

