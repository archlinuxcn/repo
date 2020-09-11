# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-onnxconverter-common
_pkgname=onnxconverter-common
pkgver=1.7.0
pkgrel=1
pkgdesc='Common utilities for ONNX converters'
arch=(any)
url='https://github.com/microsoft/onnxconverter-common'
license=(MIT)
depends=(python python-numpy python-protobuf python-onnx)
makedepends=(python-setuptools)
checkdepends=(python-pytest python-onnxruntime)
source=("https://github.com/microsoft/onnxconverter-common/archive/v$pkgver/$pkgname-$pkgver.tar.gz")
sha256sums=('d3b468b19e4318983635e4cda95985c11a554c2e5704240c513ff0c7d9e361bf')

build() {
  cd $_pkgname-$pkgver
  python setup.py build
}

check() {
  cd $_pkgname-$pkgver
  PYTHONPATH="$PWD" pytest tests
}

package() {
  cd $_pkgname-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
