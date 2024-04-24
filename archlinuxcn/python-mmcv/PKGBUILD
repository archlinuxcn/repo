# Maintainer: Butui Hu <hot123tea123@gmail.com>

_CUDA_ARCH_LIST="6.0;6.1;6.2;7.0;7.2;7.5;8.0;8.6;8.6;8.9;9.0;9.0+PTX"
_pkgname=mmcv
pkgname=(python-mmcv python-mmcv-full)
pkgver=2.2.0
pkgrel=1
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
  cp -a "${srcdir}/${_pkgname}-${pkgver}" "${srcdir}/${_pkgname}-full-${pkgver}"
}

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  MMCV_WITH_OPS=1 \
  python -m build --wheel --no-isolation

  cd "${srcdir}/${_pkgname}-full-${pkgver}"
  CC=/opt/cuda/bin/gcc \
  CXX=/opt/cuda/bin/g++ \
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
