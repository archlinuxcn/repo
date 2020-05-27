_name=hstspreload
pkgname=python-hstspreload
pkgver=2020.5.27
pkgrel=1
pkgdesc="Chromium HSTS Preload list as a Python package and updated daily"
arch=(any)
url="https://github.com/sethmlarson/hstspreload"
license=('BSD-3')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/hstspreload-2020.5.27.tar.gz")
sha256sums=('088884adc70f0efdd3002c86290e2c25c097fa49286feea7120507534f9e8be5')

build() {
  cd "$srcdir/hstspreload-2020.5.27"
  python3 setup.py build
}

package() {
  cd "$srcdir/hstspreload-2020.5.27"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

