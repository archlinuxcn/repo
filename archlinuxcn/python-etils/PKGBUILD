# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-etils
pkgver=0.9.0
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
sha512sums=('9d29f1ba87ba26e6c1c6c6410f2c2db185193acc97a9aac4f774a698282e1241595e42a5fa60960ff858da4762bf4b4c5d3b4c54ba2a996dcf41c7f5631b72df')

build() {
  cd etils-$pkgver
  python -m build --wheel --no-isolation
}

check() {
  cd etils-$pkgver
  # etils/eapp: needs simple_parsing
  # etils/enp, etils/etree/tree_utils_test.py: needs jax
  # etils/ecolab: needs mediapy
  # etils/edc/frozen_utils_test.py: needs chex
  pytest \
    --ignore etils/eapp \
    --ignore etils/ecolab \
    --ignore etils/edc/frozen_utils_test.py \
    --ignore etils/enp \
    --ignore etils/etree/tree_utils_test.py
}

package() {
  cd etils-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
}
