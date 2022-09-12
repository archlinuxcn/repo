# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-etils
pkgver=0.8.0
pkgrel=1
pkgdesc='Collection of eclectic utils for python'
url='https://github.com/google/etils'
license=('Apache')
arch=('any')
depends=('python')
makedepends=('python-build' 'python-flit-core' 'python-installer')
# Not including python-jax as build fails (https://github.com/google/jax/issues/7712)
checkdepends=('python-pytest' 'python-pytest-subtests'
              'python-numpy' 'ipython' 'absl-py' 'python-tqdm' 'python-tensorflow')
# See https://github.com/google/etils/blob/main/pyproject.toml for optional dependencies
optdepends=(
  'python-numpy: for etils.array_types, etils.ecolab, etils.enp'
  'ipython: for etils.ecolab'
  # 'python-mediapy: for etils.ecolab'
  'python-importlib_resources: for epath'
  'python-zipp: for etils.epath'
  'python-typing_extensions: for etils.epy'
  'absl-py: for etils.etqdm'
  'python-tqdm: for etils.etqdm'
  'python-dm-tree: for etils.etree.tree'
  'python-jax: for etils.etree.jax'
  'python-tensorflow: for etils.etree.nest'
)
source=("https://github.com/google/etils/archive/v$pkgver/$pkgname-$pkgver.tar.gz")
sha512sums=('c9cc3c6eec06b2a92cdeddfb7f316be19c0948853534cd89f64bbb17bab0d9c32c75565669685c5487ff1918048d5126c05c45acfac2d3b9360097c2b99ef77f')

build() {
  cd etils-$pkgver
  python -m build --wheel --no-isolation
}

check() {
  cd etils-$pkgver
  # etils/enp, etils/etree/tree_utils_test.py: needs jax
  # etils/ecolab: needs mediapy
  # etils/edc/frozen_utils_test.py: needs chex
  pytest \
    --ignore etils/ecolab \
    --ignore etils/edc/frozen_utils_test.py \
    --ignore etils/enp \
    --ignore etils/etree/tree_utils_test.py
}

package() {
  cd etils-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
}
