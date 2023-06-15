# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=netron-cli
pkgver=6.9.7
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
sha256sums=('7197c271f8d456fe9235f168f4182569135259be991b45349bd94b7279cc2b2b')

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
