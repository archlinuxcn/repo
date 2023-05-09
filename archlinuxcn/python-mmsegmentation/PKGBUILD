# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmsegmentation
pkgname=python-mmsegmentation
pkgver=1.0.0
pkgrel=1
epoch=1
pkgdesc='OpenMMLab Semantic Segmentation Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmsegmentation'
license=('Apache')
depends=(
  python-matplotlib
  python-mmpretrain
  python-mmcv
  python-numpy
  python-prettytable
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmsegmentation/archive/v${pkgver}.tar.gz")
sha512sums=('3555d52011d44f0aef1403ac630fc0a0137eb2b5b69bec02896cf04797789822e294f98582f0590521eacbbaff250c7e806dce664e3b714df76e3af969e8e915')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  # remove unused .mim and tests dir
  rm -rfv "${pkgdir}${site_packages}/mmseg/.mim"
  rm -rfv "${pkgdir}${site_packages}/tests"
}
# vim:set ts=2 sw=2 et:
