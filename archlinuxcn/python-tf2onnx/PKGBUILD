# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-tf2onnx
pkgver=1.9.1
pkgrel=2
pkgdesc='Convert TensorFlow models to ONNX'
arch=(any)
url='https://github.com/onnx/tensorflow-onnx'
license=(MIT)
depends=(python python-tensorflow python-numpy python-onnx python-requests python-six)
makedepends=(python-setuptools python-build python-install python-wheel)
checkdepends=(python-pytest python-graphviz python-parameterized python-yaml python-onnxruntime)
source=("https://github.com/onnx/tensorflow-onnx/archive/v$pkgver/tf2onnx-v$pkgver.tar.gz"
        'larger-tolerance.diff')
sha256sums=('e3bb05f0a2d0afe4d4bda4946bd04d0262dc7780a93e0ab5c9a5050f905ca869'
            '171684b938833d544e04fef6a420ca209a4785b40377b99c8a37336bada5d3f1')

prepare() {
  cd tensorflow-onnx-$pkgver
  sed -i -r 's#--cov\S+##' setup.cfg
  sed -i "s#'pytest-runner'##" setup.py
  patch -Np1 -i ../larger-tolerance.diff
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
