# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-tf2onnx
epoch=1
pkgver=1.13.0
pkgrel=1
pkgdesc='Convert TensorFlow models to ONNX'
arch=(any)
url='https://github.com/onnx/tensorflow-onnx'
license=(MIT)
depends=(python python-tensorflow python-numpy python-onnx python-requests python-six python-flatbuffers)
makedepends=(python-setuptools python-build python-installer python-wheel)
checkdepends=(python-pytest python-graphviz python-parameterized python-yaml python-onnxruntime)
source=("https://github.com/onnx/tensorflow-onnx/archive/v$pkgver/tf2onnx-v$pkgver.tar.gz"
        "onnxruntime.diff")
sha256sums=('2b3ffb792e1e9bb4390040c9e29856ef864a59f575727df61ce379e214959a21'
            '7e8ab46940aff7cac8d535436c8e201f37c66637416ae9b795706a4c3dd01232')

prepare() {
  cd tensorflow-onnx-$pkgver

  sed -i -r 's#--cov\S+##' setup.cfg
  sed -i "s#'pytest-runner'##" setup.py

  # https://github.com/onnx/tensorflow-onnx/issues/1977
  sed -i 's#flatbuffers~=1.12#flatbuffers#' setup.py

  # The latest upstream tag may not sync with the version file
  echo $pkgver > VERSION_NUMBER

  patch -Np1 -i ../onnxruntime.diff
}

build() {
  cd tensorflow-onnx-$pkgver
  python -m build --wheel --no-isolation
}

check() {
  cd tensorflow-onnx-$pkgver
  # Apparently the failure is caused by new operators in TensorFlow lite 2.10.0 [1][2]
  # [1] https://github.com/tensorflow/tensorflow/commit/cac33fd25c1df270758a66fd0dadba5c973abf9a
  # [2] https://github.com/tensorflow/tensorflow/commit/12f38bba6659b417f5408f24ebf267e05c738beb
  PYTHONPATH="$PWD" pytest tests -k 'not test_unsorted_segment_ops'
}

package() {
  cd tensorflow-onnx-$pkgver
  python -m installer --destdir="$pkgdir" --compile-bytecode 0 --compile-bytecode 1 --compile-bytecode 2 dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
