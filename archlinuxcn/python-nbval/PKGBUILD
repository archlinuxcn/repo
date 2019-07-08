# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-nbval
_pkgname=nbval
pkgver=0.9.2
pkgrel=2
pkgdesc='A py.test plugin to validate Jupyter notebooks'
arch=(any)
url='https://github.com/computationalmodelling/nbval'
license=(BSD)
depends=(python python-pytest python-six python-jupyter_client
         jupyter-nbformat python-ipykernel python-coverage)
makedepends=(python-setuptools)
checkdepends=(python-doit python-matplotlib python-sympy python-pytest-cov)
source=("https://github.com/computationalmodelling/nbval/archive/$pkgver/$pkgname-$pkgver.tar.gz")
sha256sums=('35bfaa449037a685aa0f0bb1fa252db77aa309bc3dcd0a288e9402d5505d8e61')

build() {
  cd $_pkgname-$pkgver
  python setup.py build
}

check() {
  cd $_pkgname-$pkgver
  # needed for the pytest plugin entry point
  python setup.py install --root="$srcdir"/tmp_install
  PYTHONPATH="$srcdir"/tmp_install/usr/lib/python3.7/site-packages doit test
}

package() {
  cd $_pkgname-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
