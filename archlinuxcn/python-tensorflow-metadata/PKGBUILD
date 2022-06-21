# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-tensorflow-metadata
pkgver=1.9.0
pkgrel=1
pkgdesc='Utilities for passing TensorFlow-related metadata between tools'
arch=(any)
url='https://github.com/tensorflow/metadata'
license=(Apache)
depends=(python absl-py python-googleapis-common-protos python-protobuf)
makedepends=(python-setuptools bazel)
source=(https://github.com/tensorflow/metadata/archive/v$pkgver/$pkgname-$pkgver.tar.gz)
sha256sums=('ef6805eecb159753431449fb15519f22f06d7395ed34a2b615d6e4f773206828')

build() {
  cd metadata-$pkgver
  python setup.py build
}

package() {
  cd metadata-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
