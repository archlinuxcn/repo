# Maintainer: Butui Hu <hot123tea123@gmail.com>

_CUDA_ARCH_LIST="5.2;5.3;6.0;6.1;6.2;7.0;7.0+PTX;7.2;7.2+PTX;7.5;7.5+PTX;8.0;8.0+PTX;8.6;8.6+PTX"
_pkgname=mmcv
pkgname=(python-mmcv python-mmcv-full)
pkgver=1.2.4
pkgrel=1
pkgdesc='OpenMMLab Computer Vision Foundation'
arch=('x86_64')
url='https://github.com/open-mmlab/mmcv'
license=('Apache')
depends=(
  python-addict
  python-lmdb
  python-pillow
)
makedepends=(
  cuda
  cython
  python-pytorch-cuda
  python-setuptools
)
optdepends=(
  "opencv: optional image backend"
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmcv/archive/v${pkgver}.tar.gz")
sha512sums=('6735f574eaa8e317d628ea3cc9057a1a8665a214af734377d189252ddfbfaf9d78ee77369efdc8f4c9f8ee094966133c1d12f7826a39cf0ab4cba63e8261db0a')

build() {
  cp -a "${_pkgname}-${pkgver}" "${_pkgname}-full-${pkgver}"
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build

  cd "${srcdir}/${_pkgname}-full-${pkgver}"
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  MMCV_WITH_OPS=1 FORCE_CUDA=1 python setup.py build
}

package_python-mmcv() {
  pkgdesc+="(lite version, without cuda ops)"
  depends+=(python-pytorch)

  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}

package_python-mmcv-full() {
  pkgdesc+=" (full version, with full features, include cuda ops)"
  depends+=(cuda python-pytorch-cuda)
  provides=(python-mmcv=${pkgver})
  conflicts=(python-mmcv)

  cd "${_pkgname}-full-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
