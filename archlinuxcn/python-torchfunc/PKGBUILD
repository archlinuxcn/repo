# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-torchfunc
pkgver=0.2.0
pkgrel=1
pkgdesc='PyTorch functions and utilities to make your life easier'
url='https://github.com/szymonmaszke/torchfunc'
license=('MIT')
arch=('any')
depends=('python-pytorch')
makedepends=('python-setuptools' 'python-build' 'python-installer' 'python-wheel')
checkdepends=('python-pytest' 'python-torchvision')
source=("https://github.com/szymonmaszke/torchfunc/archive/v$pkgver/$pkgname-$pkgver.tar.gz")
sha512sums=('b3ab75b0277fa5c67465f39a6e7cadcca3522c585b16faf46819b8ac434ddd1f4c2a918f8971f3c98b26f4b7019f14349d5961a1127fc65d8820e759367cc8e5')

build() {
  cd torchfunc-$pkgver
  python -m build --wheel --no-isolation
}

check() {
  cd torchfunc-$pkgver
  pytest
}

package() {
  cd torchfunc-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
  rm -rf "${pkgdir}"/usr/lib/python*/site-packages/tests
}
