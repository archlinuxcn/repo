# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-tf2onnx
pkgver=1.10.1
pkgrel=1
pkgdesc='Convert TensorFlow models to ONNX'
arch=(any)
url='https://github.com/onnx/tensorflow-onnx'
license=(MIT)
depends=(python python-tensorflow python-numpy python-onnx python-requests python-six)
makedepends=(python-setuptools python-build python-install python-wheel)
checkdepends=(python-pytest python-graphviz python-parameterized python-yaml python-onnxruntime)
source=("https://github.com/onnx/tensorflow-onnx/archive/v$pkgver/tf2onnx-v$pkgver.tar.gz")
sha256sums=('60f342b8f5a67482a067b3fa7aa26110a806bba82ddd0cb188189e097de95835')

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
  PYTHONPATH="$PWD" pytest tests
}

package() {
  cd tensorflow-onnx-$pkgver
  python -m install --destdir="$pkgdir" --skip-build --verify-dependencies
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
