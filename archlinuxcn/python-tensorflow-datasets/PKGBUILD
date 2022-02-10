# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-tensorflow-datasets
pkgver=4.5.2
pkgrel=1
pkgdesc='A collection of datasets ready to use with TensorFlow, Jax, ...'
arch=(any)
url='https://github.com/tensorflow/datasets'
license=(Apache)
depends=(python absl-py python-{dill,numpy,promise,protobuf,requests,six,tensorflow-metadata,termcolor,toml,tqdm})
makedepends=(python-setuptools)
source=(https://github.com/tensorflow/datasets/archive/v$pkgver/$pkgname-$pkgver.tar.gz)
sha256sums=('e0d82d4874f453233267384260d38bcd50dd8a517c16e07131147a642aba6a15')

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
