# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-tensorflow-metadata
pkgver=1.10.0
pkgrel=1
pkgdesc='Utilities for passing TensorFlow-related metadata between tools'
arch=(any)
url='https://github.com/tensorflow/metadata'
license=(Apache)
depends=(python absl-py python-googleapis-common-protos python-protobuf)
makedepends=(python-setuptools bazel)
source=(https://github.com/tensorflow/metadata/archive/v$pkgver/$pkgname-$pkgver.tar.gz)
sha256sums=('e7aa81aa01433e2a75c11425affd55125b64f384baf96b71eeb3a88dca8cf2ae')

build() {
  cd metadata-$pkgver
  python setup.py build
}

package() {
  cd metadata-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
