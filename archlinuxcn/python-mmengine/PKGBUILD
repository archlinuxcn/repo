# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmengine
pkgname=python-mmengine
pkgver=0.10.6
pkgrel=1
pkgdesc='OpenMMLab Foundational Library for Training Deep Learning Models'
arch=('any')
url='https://github.com/open-mmlab/mmengine'
license=('Apache-2.0')
depends=(
  python-addict
  python-matplotlib
  python-numpy
  python-termcolor
  python-yaml
  yapf
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmengine/archive/refs/tags/v${pkgver}.tar.gz"
        "https://github.com/open-mmlab/mmengine/pull/1610.patch"
)
sha512sums=('2df55a56737cbf8df3ee5c322cca09c9d2c78a01ee1d9fb78079a9db5ea703a41b8d7b682422f52f4681101efdcf976b3d235edea2b639999275d7596ed13f80'
            'fbb36fdd3715f41ce5cefe4fbc8deaccf2a125d72d69acf5574fb09f0f5fadef7b874a52623bd38656c25577d0573e2ee31729e8217b5f9e4c5d1a83e6eb9719')

prepare() {
  cd "${_pkgname}-${pkgver}"
  patch -p1 -i ${srcdir}/1610.patch
  sed -i "s/version=get_version()/version='$pkgver'/" setup.py
}

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
