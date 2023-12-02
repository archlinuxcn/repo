# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=netron-cli
pkgver=7.3.2
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
sha256sums=('a6af407bd100ef64f3f098538a95c121f7d0dbc20e2430e23ba37214444cdb85')

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
