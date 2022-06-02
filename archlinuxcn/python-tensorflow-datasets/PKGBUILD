# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-tensorflow-datasets
pkgver=4.6.0
pkgrel=1
pkgdesc='A collection of datasets ready to use with TensorFlow, Jax, ...'
arch=(any)
url='https://github.com/tensorflow/datasets'
license=(Apache)
depends=(python absl-py python-{dill,numpy,promise,protobuf,requests,six,tensorflow-metadata,termcolor,toml,tqdm})
makedepends=(python-setuptools)
source=(https://github.com/tensorflow/datasets/archive/v$pkgver/$pkgname-$pkgver.tar.gz)
sha256sums=('42fcb55829f96cfc7f0ee74a502950b052149811bb867371880b8235e7d8d6d3')

prepare() {
  cd datasets-$pkgver
  mv -vf tensorflow_datasets/{version_stable,version}.py
}

build() {
  cd datasets-$pkgver
  python setup.py build
}

package() {
  cd datasets-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
