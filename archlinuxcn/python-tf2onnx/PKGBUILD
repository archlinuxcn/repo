# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-tf2onnx
pkgver=1.12.1
pkgrel=1
pkgdesc='Convert TensorFlow models to ONNX'
arch=(any)
url='https://github.com/onnx/tensorflow-onnx'
license=(MIT)
depends=(python python-tensorflow python-numpy python-onnx python-requests python-six)
makedepends=(python-setuptools python-build python-installer python-wheel)
checkdepends=(python-pytest python-graphviz python-parameterized python-yaml python-onnxruntime)
source=("https://github.com/onnx/tensorflow-onnx/archive/v$pkgver/tf2onnx-v$pkgver.tar.gz"
        "onnxruntime.diff")
sha256sums=('103948bf96d8861ebb9fbcc35bb46090007fc970de2411db8388ceb494e29b4a'
            '7e8ab46940aff7cac8d535436c8e201f37c66637416ae9b795706a4c3dd01232')

prepare() {
  cd tensorflow-onnx-$pkgver

  sed -i -r 's#--cov\S+##' setup.cfg
  sed -i "s#'pytest-runner'##" setup.py

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
  PYTHONPATH="$PWD" pytest tests
}

package() {
  cd tensorflow-onnx-$pkgver
  python -m installer --destdir="$pkgdir" --compile-bytecode 0 --compile-bytecode 1 --compile-bytecode 2 dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
