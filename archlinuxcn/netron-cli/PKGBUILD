# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=netron-cli
pkgver=9.3.1
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
sha256sums=('612d8a064d0c7e166b47208c41bb8ac2ae7f95d5a5f0d659e3f41d82c3cd5507')

build() {
  cd netron-$pkgver
  python package.py build version
  python -m build --wheel --no-isolation --outdir dist/pypi dist/pypi
}

package() {
  cd netron-$pkgver
  python -m installer --destdir="$pkgdir" dist/pypi/*.whl
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
