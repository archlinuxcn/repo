# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-tensorflow-metadata
pkgver=1.7.0
pkgrel=1
pkgdesc='Utilities for passing TensorFlow-related metadata between tools'
arch=(any)
url='https://github.com/tensorflow/metadata'
license=(Apache)
depends=(python absl-py python-googleapis-common-protos python-protobuf)
makedepends=(python-setuptools bazel)
source=(https://github.com/tensorflow/metadata/archive/v$pkgver/$pkgname-$pkgver.tar.gz)
sha256sums=('9c64ad3813afbc7466e0eefba33359968b8fe33a375b8b5b87f340dd3abe56c7')

build() {
  cd metadata-$pkgver
  python setup.py build
}

package() {
  cd metadata-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
