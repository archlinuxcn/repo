# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-tf2onnx
epoch=1
pkgver=1.12.0
pkgrel=2
pkgdesc='Convert TensorFlow models to ONNX'
arch=(any)
url='https://github.com/onnx/tensorflow-onnx'
license=(MIT)
depends=(python python-tensorflow python-numpy python-onnx python-requests python-six)
makedepends=(python-setuptools python-build python-installer python-wheel)
checkdepends=(python-pytest python-graphviz python-parameterized python-yaml python-onnxruntime)
source=("https://github.com/onnx/tensorflow-onnx/archive/v.$pkgver/tf2onnx-v$pkgver.tar.gz"
        "onnxruntime.diff")
sha256sums=('958c1bd50131e91d91a79629cfe70e13a02295a6c81486598b74cef9ba2000c6'
            '7e8ab46940aff7cac8d535436c8e201f37c66637416ae9b795706a4c3dd01232')

prepare() {
  cd tensorflow-onnx-v.$pkgver

  sed -i -r 's#--cov\S+##' setup.cfg
  sed -i "s#'pytest-runner'##" setup.py

  # The latest upstream tag may not sync with the version file
  echo $pkgver > VERSION_NUMBER

  patch -Np1 -i ../onnxruntime.diff
}

build() {
  cd tensorflow-onnx-v.$pkgver
  python -m build --wheel --no-isolation
}

check() {
  cd tensorflow-onnx-v.$pkgver
  PYTHONPATH="$PWD" pytest tests
}

package() {
  cd tensorflow-onnx-v.$pkgver
  python -m installer --destdir="$pkgdir" --compile-bytecode 0 --compile-bytecode 1 --compile-bytecode 2 dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
