# Maintainer: Butui Hu <hot123tea123@gmail.com>

_CUDA_ARCH_LIST="7.5;8.0;8.6;8.7;8.9;9.0;10.0;10.3;12.0;12.1;12.1+PTX"
_pkgname=mmcv
pkgname=(python-mmcv python-mmcv-full)
pkgver=2.2.0
pkgrel=5
epoch=1
pkgdesc='OpenMMLab Computer Vision Foundation'
arch=('x86_64')
url='https://github.com/open-mmlab/mmcv'
license=('Apache-2.0')
depends=(
  python-addict
  python-mmengine
  python-numpy
  python-opencv
  python-pillow
  python-yaml
  yapf
)
makedepends=(
  cuda
  cython
  python-build
  python-installer
  python-pytorch-cuda
  python-setuptools
  python-sympy
  python-wheel
  numactl
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmcv/archive/v${pkgver}.tar.gz"
)
sha512sums=('e2899272a2b9015f8a73af15d36b7d2ccf2a56a69dbd9f02186b31a5939a2b8e257a15a68957599ede48d688475e344e23b3cae749b79c5e405a0d2aa0937306')
prepare() {
  # fix glog error
  sed -i "s/define_macros = \[\]/define_macros = [('GLOG_USE_GLOG_EXPORT', None)]/g" "${_pkgname}-${pkgver}/setup.py"
  # dirty hack
  sed -i 's,THC/THCAtomics.cuh,ATen/cuda/Atomic.cuh,' "${_pkgname}-${pkgver}/mmcv/ops/csrc/common/pytorch_cuda_helper.hpp"
  sed -i 's,THC/THCAtomics.cuh,ATen/cuda/Atomic.cuh,' "${_pkgname}-${pkgver}/mmcv/ops/csrc/pytorch/cuda/ms_deform_attn_cuda.cu"
  # setting version
  sed -i "s/version=get_version()/version='$pkgver'/" "${_pkgname}-${pkgver}/setup.py"
  cp -a "${srcdir}/${_pkgname}-${pkgver}" "${srcdir}/${_pkgname}-full-${pkgver}"
}

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  MMCV_WITH_OPS=1 \
  python -m build --wheel --no-isolation

  cd "${srcdir}/${_pkgname}-full-${pkgver}"
  FORCE_CUDA=1 \
  MMCV_WITH_OPS=1 \
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  python -m build --wheel --no-isolation
}

package_python-mmcv() {
  pkgdesc+="(cpu version, without cuda ops)"
  depends+=(python-pytorch)

  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
}

package_python-mmcv-full() {
  pkgdesc+=" (full version, with full features, include cuda ops)"
  depends+=(cuda python-pytorch-cuda libcudart.so)
  provides=(python-mmcv=${pkgver})
  conflicts=(python-mmcv)

  cd "${_pkgname}-full-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
# vim:set ts=2 sw=2 et:
