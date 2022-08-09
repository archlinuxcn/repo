# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-etils
pkgver=0.7.0
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
sha512sums=('7497807a43ffbe0ab7d0f011cb340729a024024690495a630147094ae5933e607b1dd3912c81b10a64dc2760a9191106684427d122ed8cb64e784fad978d2fa4')

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
