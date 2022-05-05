# Maintainer: Chih-Hsuan Yen <base64_decode("eWFuMTIxMjUgQVQgYXJjaGxpbnV4IERPVCBvcmc=")>

pkgname=python-onnx2pytorch
pkgver=0.4.1
pkgrel=1
pkgdesc='Library to transform onnx model to pytorch'
arch=(any)
url='https://github.com/ToriML/onnx2pytorch'
license=(Apache)
depends=(python python-pytorch python-onnx python-torchvision)
makedepends=(python-setuptools python-build python-installer python-wheel)
checkdepends=(python-pytest python-onnxruntime)
source=("https://github.com/ToriML/onnx2pytorch/archive/v$pkgver/onnx2pytorch-v$pkgver.tar.gz"
        onnxruntime-specify-provider.diff)
sha256sums=('afda9f25f3ea639de57a3b432c970ed62878a73084db5febac5c6c2c4c98ba9b'
            'e446bd33cfb0ad000d2d4b73e16feb8bbdb245f41b8635be9a9a52d7a911fc52')

prepare() {
  cd onnx2pytorch-$pkgver
  patch -Np1 -i ../onnxruntime-specify-provider.diff
}

build() {
  cd onnx2pytorch-$pkgver
  python -m build --wheel --no-isolation
}

check() {
  cd onnx2pytorch-$pkgver
  # InstanceNorm is broken with pytorch 1.11, in which relevant classes are changed
  # test_lstm crashes with current pytorch https://bugs.archlinux.org/task/74593
  PYTHONPATH="$PWD" pytest tests \
    --ignore tests/onnx2pytorch/operations/test_instancenorm.py \
    --ignore tests/onnx2pytorch/convert/test_lstm.py
}

package() {
  cd onnx2pytorch-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
