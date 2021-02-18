# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-tf2onnx
pkgver=1.8.3
pkgrel=1
pkgdesc='Convert TensorFlow models to ONNX'
arch=(any)
url='https://github.com/onnx/tensorflow-onnx'
license=(MIT)
depends=(python python-tensorflow python-numpy python-onnx python-requests python-six)
makedepends=(python-setuptools python-build python-install python-wheel)
checkdepends=(python-pytest python-graphviz python-parameterized python-yaml python-onnxruntime)
source=("https://github.com/onnx/tensorflow-onnx/archive/v$pkgver/tf2onnx-v$pkgver.tar.gz")
sha256sums=('9fdbd4e3cf2bd9f349ce2eb4700e7725d639316d405ed9f66a137bed2f0a2ba4')

prepare() {
  cd tensorflow-onnx-$pkgver
  sed -i -r 's#--cov\S+##' setup.cfg
  sed -i "s#'pytest-runner'##" setup.py
}

build() {
  cd tensorflow-onnx-$pkgver
  python -m build --wheel --no-isolation
  python -m install --cache dist/*.whl
}

check() {
  cd tensorflow-onnx-$pkgver
  # Some tests fail most likely due to changes in NumPy 1.20. Actually TensorFlow does not
  # completely work with NumPy 1.20 either [1].
  # https://github.com/tensorflow/tensorflow/issues/44654#issuecomment-771919878
  PYTHONPATH="$PWD" pytest tests -k 'not test_unsorted_segment_ops'
}

package() {
  cd tensorflow-onnx-$pkgver
  python -m install --destdir="$pkgdir" --skip-build --verify-dependencies
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
