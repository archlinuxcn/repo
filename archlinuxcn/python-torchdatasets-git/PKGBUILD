# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-torchdatasets-git
pkgver=0.2.0.25.g0389fee
pkgrel=1
pkgdesc='PyTorch dataset extended with map, cache etc. (tensorflow.data like)'
url='https://github.com/szymonmaszke/torchdatasets'
license=('MIT')
arch=('any')
depends=('python-pytorch')
makedepends=('python-setuptools' 'python-build' 'python-installer' 'python-wheel' 'git')
checkdepends=('python-pytest' 'python-torchvision' 'python-torchfunc')
provides=("python-torchdatasets=$pkgver")
conflicts=("python-torchdatasets")
source=("git+https://github.com/szymonmaszke/torchdatasets.git")
sha512sums=('SKIP')

prepare() {
  cd torchdatasets
  # TODO: report forgotten renames to upstream
  sed -i 's#\btorchdata\b#torchdatasets#g' tests/*.py
}

pkgver() {
  cd torchdatasets
  git describe --tags --always | sed "s/-/./g;s/^v//"
}

build() {
  cd torchdatasets
  python -m build --wheel --no-isolation
}

check() {
  cd torchdatasets
  pytest
}

package() {
  cd torchdatasets
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
  rm -rf "${pkgdir}"/usr/lib/python*/site-packages/tests
}
