# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-onnxconverter-common
_pkgname=onnxconverter-common
pkgver=1.8.1
pkgrel=1
pkgdesc='Common utilities for ONNX converters'
arch=(any)
url='https://github.com/microsoft/onnxconverter-common'
license=(MIT)
depends=(python python-numpy python-protobuf python-onnx)
makedepends=(python-setuptools)
checkdepends=(python-pytest python-onnxruntime)
source=("https://github.com/microsoft/onnxconverter-common/archive/v$pkgver/$pkgname-$pkgver.tar.gz")
sha256sums=('f95f2a2d1fedc20cccbc820d4f63cbe84e287a5bd8c863ced400ae73946e13e6')

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
