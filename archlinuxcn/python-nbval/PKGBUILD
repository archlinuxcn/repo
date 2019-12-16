# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-nbval
_pkgname=nbval
pkgver=0.9.4
pkgrel=1
pkgdesc='A py.test plugin to validate Jupyter notebooks'
arch=(any)
url='https://github.com/computationalmodelling/nbval'
license=(BSD)
depends=(python python-pytest python-six python-jupyter_client
         jupyter-nbformat python-ipykernel python-coverage)
makedepends=(python-setuptools)
checkdepends=(python-doit python-matplotlib python-sympy python-pytest-cov)
source=("https://github.com/computationalmodelling/nbval/archive/$pkgver/$pkgname-$pkgver.tar.gz")
sha256sums=('34a9d53dc7da0420ba365a1d7adfee620346bdaea3088c80ddfdfc3f4b886bd9')

build() {
  cd $_pkgname-$pkgver
  python setup.py build
}

check() {
  cd $_pkgname-$pkgver
  # needed for the pytest plugin entry point
  python setup.py install --root="$srcdir"/tmp_install
  site_packages_path=$(python -c 'import site; print(site.getsitepackages()[0])')
  PYTHONPATH="$srcdir"/tmp_install$site_packages_path doit test
}

package() {
  cd $_pkgname-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
