# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmcv
pkgname=(python-mmcv python-mmcv-full)
pkgver=1.1.1
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
sha512sums=('33aeca9856c6e3afb3a64bb6c4b3dca59ca9d1f6f66e80f198e1ea5ed8b1a0d01d6a51599b8da44b1a4b1d80c8998bdd349a3613427eba6dd2aca66667ea7618')

build() {
  cp -a "${_pkgname}-${pkgver}" "${_pkgname}-full-${pkgver}"
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build

  cd "${srcdir}/${_pkgname}-full-${pkgver}"
  TORCH_CUDA_ARCH_LIST="5.2;5.3;6.0;6.0+PTX;6.1;6.1+PTX;6.2;6.2+PTX;7.0;7.0+PTX;7.2;7.2+PTX;7.5;7.5+PTX;8.0;8.0+PTX" \
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
