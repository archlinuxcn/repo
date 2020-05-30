_name=hstspreload
pkgname=python-hstspreload
pkgver=2020.5.30
pkgrel=1
pkgdesc="Chromium HSTS Preload list as a Python package and updated daily"
arch=(any)
url="https://github.com/sethmlarson/hstspreload"
license=('BSD-3')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/hstspreload-2020.5.30.tar.gz")
sha256sums=('d44cb7a113806e55f6e08f1dfac0254f1db2933989172fa481e59470c47340f3')

build() {
  cd "$srcdir/hstspreload-2020.5.30"
  python3 setup.py build
}

package() {
  cd "$srcdir/hstspreload-2020.5.30"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

