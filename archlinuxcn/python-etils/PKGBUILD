# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

pkgname=python-etils
pkgver=0.6.0
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
sha512sums=('a84c54dc81242fa12fe48b875c6f9b74acfe885629be09f5b9bf05d11f2d4e468f252c721cfd50eb137694ed44190513b0b1b85cfdc16440e8453bd74277702a')

build() {
  cd etils-$pkgver
  python -m build --wheel --no-isolation
}

check() {
  cd etils-$pkgver
  pacman -Qi python-six
  # etils/array_types/typing_test.py, etils/enp, etils/etree/tree_utils_test.py: needs jax
  # etils/ecolab: needs mediapy
  # etils/edc/frozen_utils_test.py: needs chex
  # test_repr, test_resource_path: broken on Python 3.10 https://github.com/google/etils/issues/143
  pytest \
    --ignore etils/array_types/typing_test.py \
    --ignore etils/ecolab \
    --ignore etils/edc/frozen_utils_test.py \
    --ignore etils/enp \
    --ignore etils/etree/tree_utils_test.py \
    -k 'not test_repr and not test_resource_path'
}

package() {
  cd etils-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
}
