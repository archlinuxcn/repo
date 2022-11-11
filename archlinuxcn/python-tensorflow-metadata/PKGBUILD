# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-tensorflow-metadata
pkgver=1.11.0
pkgrel=1
pkgdesc='Utilities for passing TensorFlow-related metadata between tools'
arch=(any)
url='https://github.com/tensorflow/metadata'
license=(Apache)
depends=(python absl-py python-googleapis-common-protos python-protobuf)
makedepends=(python-setuptools bazel)
source=(https://github.com/tensorflow/metadata/archive/v$pkgver/$pkgname-$pkgver.tar.gz)
sha256sums=('9b0363f0dd7d479dffaa9c7a6d8bae81069adeeb665f196a056233f4cbd3fe1b')

build() {
  cd metadata-$pkgver
  python setup.py build
}

package() {
  cd metadata-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
