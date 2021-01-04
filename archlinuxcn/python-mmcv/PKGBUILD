# Maintainer: Butui Hu <hot123tea123@gmail.com>

_CUDA_ARCH_LIST="5.2;5.3;6.0;6.1;6.2;7.0;7.0+PTX;7.2;7.2+PTX;7.5;7.5+PTX;8.0;8.0+PTX;8.6;8.6+PTX"
_pkgname=mmcv
pkgname=(python-mmcv python-mmcv-full)
pkgver=1.2.5
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
  python-pip
  python-pytorch-cuda
  python-setuptools
  python-wheel
)
optdepends=(
  "opencv: optional image backend"
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmcv/archive/v${pkgver}.tar.gz")
sha512sums=('d6408228fbcaddae3e39c3ec121e148103740771753679fcd21bea0f06ced41123ec8586d9cc89186bdc931c824c3ba9987ec699f692796001aa39747a9d756e')

build() {
  cp -a "${_pkgname}-${pkgver}" "${_pkgname}-full-${pkgver}"
  cd "${srcdir}/${_pkgname}-${pkgver}"
  MMCV_WITH_OPS=1 python setup.py bdist_wheel

  cd "${srcdir}/${_pkgname}-full-${pkgver}"
  TORCH_CUDA_ARCH_LIST=${_CUDA_ARCH_LIST} \
  MMCV_WITH_OPS=1 FORCE_CUDA=1 python setup.py bdist_wheel
}

package_python-mmcv() {
  pkgdesc+="(cpu version, without cuda ops)"
  depends+=(python-pytorch)

  cd "${_pkgname}-${pkgver}"
  PIP_CONFIG_FILE=/dev/null pip install --isolated --root="${pkgdir}" --ignore-installed --no-deps dist/*.whl
  python -O -m compileall "${pkgdir}/usr/lib"
}

package_python-mmcv-full() {
  pkgdesc+=" (full version, with full features, include cuda ops)"
  depends+=(cuda python-pytorch-cuda)
  provides=(python-mmcv=${pkgver})
  conflicts=(python-mmcv)

  cd "${_pkgname}-full-${pkgver}"
  PIP_CONFIG_FILE=/dev/null pip install --isolated --root="${pkgdir}" --ignore-installed --no-deps dist/*.whl
  python -O -m compileall "${pkgdir}/usr/lib"
}
# vim:set ts=2 sw=2 et:
