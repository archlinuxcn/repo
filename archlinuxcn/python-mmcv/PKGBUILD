# Maintainer: Butui Hu <hot123tea123@gmail.com>

_CUDA_ARCH_LIST="5.2;5.3;6.0;6.1;6.2;7.0;7.0+PTX;7.2;7.2+PTX;7.5;7.5+PTX;8.0;8.0+PTX;8.6;8.6+PTX"
_pkgname=mmcv
pkgname=(python-mmcv python-mmcv-full)
pkgver=1.3.5
pkgrel=1
pkgdesc='OpenMMLab Computer Vision Foundation'
arch=('x86_64')
url='https://github.com/open-mmlab/mmcv'
license=('Apache')
depends=(
  python-addict
  python-lmdb
  python-opencv
  python-pillow
)
makedepends=(
  cuda
  cython
  python-pip
  python-pytorch-cuda
  python-setuptools
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmcv/archive/v${pkgver}.tar.gz")
sha512sums=('66329eb08d0f86d2dc9848d678db821aa8340f14fdd599e6818a87bf1f30148156b50908b25574c75dfc4c49a5cdeaa11417dcf7de7954def7db5cca089327ca')

prepare() {
  cp -a "${_pkgname}-${pkgver}" "${_pkgname}-full-${pkgver}"
}

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  MMCV_WITH_OPS=1 python setup.py build_py
  MMCV_WITH_OPS=1 python setup.py build_ext
  
  cd "${srcdir}/${_pkgname}-full-${pkgver}"
  FORCE_CUDA=1 \
  MMCV_WITH_OPS=1 \
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  python setup.py build_py
  FORCE_CUDA=1 \
  MMCV_WITH_OPS=1 \
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  python setup.py build_ext
}

package_python-mmcv() {
  pkgdesc+="(cpu version, without cuda ops)"
  depends+=(python-pytorch)

  cd "${_pkgname}-${pkgver}"
  MMCV_WITH_OPS=1 python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}

package_python-mmcv-full() {
  pkgdesc+=" (full version, with full features, include cuda ops)"
  depends+=(cuda python-pytorch-cuda)
  provides=(python-mmcv=${pkgver})
  conflicts=(python-mmcv)

  cd "${_pkgname}-full-${pkgver}"
  FORCE_CUDA=1 \
  MMCV_WITH_OPS=1 \
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
