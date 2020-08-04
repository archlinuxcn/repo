# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmcv
pkgname=(python-mmcv python-mmcv-full)
pkgver=1.0.5
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
  python-setuptools
)
optdepends=(
  "opencv: optional image backend"
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmcv/archive/v${pkgver}.tar.gz")
sha512sums=('e76c6b2ef73d4d5ccc10d705fd71affa909c93e72a61f9bc156db17a99b28270978ceee1de2efcb8a2c98467f49f7df1f12e0ea0b0d776a58e04704de6bb2ded')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

build() {
  cp -a "${_pkgname}-${pkgver}" "${_pkgname}-full-${pkgver}"
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build

  cd "${srcdir}/${_pkgname}-full-${pkgver}"
  MMCV_WITH_OPS=1 python setup.py build
}

package_python-mmcv() {
  pkgdesc+="(lite version, without cuda ops)"

  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}

package_python-mmcv-full() {
  pkgdesc+=" (full version, with full features, include cuda ops)"
  depends+=(cuda)
  provides=(python-mmcv=${pkgver})
  conflicts=(python-mmcv)

  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
