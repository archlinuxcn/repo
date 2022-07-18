# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=netron-cli
pkgver=5.9.4
pkgrel=1
pkgdesc='Visualizer for neural network, deep learning, and machine learning models (CLI only)'
url='https://netron.app/'
arch=(any)
license=(MIT)
depends=(python)
makedepends=(python-setuptools python-build python-installer python-wheel)
optdepends=(
  'python-onnx: serializing ONNX models'
  'python-pytorch: serializing PyTorch models'
)
source=(https://github.com/lutzroeder/netron/archive/v$pkgver/netron-$pkgver.tar.gz)
sha256sums=('aed5dfd423ad5201e8b3feb3b327e5b8de513298570c6082174cdf7d90346c19')

prepare() {
  cd netron-$pkgver
  # Use dependencies from Arch
  sed -i '/python -m pip/d' Makefile
  # We don't need node_modules...trick Makefile
  mkdir node_modules
}

build() {
  cd netron-$pkgver
  make build_python
}

package() {
  cd netron-$pkgver
  python -m installer --destdir="$pkgdir" dist/pypi/*.whl
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
