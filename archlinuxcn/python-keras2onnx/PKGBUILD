# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-keras2onnx
_pkgname=keras-onnx
pkgver=1.7.0.40.g0c037e5
# The latest stable version requires quite a few patches for compatibility
# with the latest TensorFlow/ONNXRuntime
_commit=0c037e5968c0b5dc6bb12dcf4edcfdeeaf4c964f
pkgrel=1
pkgdesc='Convert tf.keras/Keras models to ONNX'
arch=(any)
url='https://github.com/onnx/keras-onnx'
license=(MIT)
depends=(python python-numpy python-protobuf python-requests python-onnx
         python-onnxconverter-common python-fire python-tensorflow)
makedepends=(python-setuptools git)
checkdepends=(python-pytest)
source=("git+https://github.com/onnx/keras-onnx.git#commit=$_commit")
sha256sums=('SKIP')

pkgver() {
  cd $_pkgname
  git describe --always --tags | sed "s/^v//;s/-/./g"
}

build() {
  cd $_pkgname
  python setup.py build
}

check() {
  cd $_pkgname
  PYTHONPATH="$PWD" pytest tests
}

package() {
  cd $_pkgname
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
