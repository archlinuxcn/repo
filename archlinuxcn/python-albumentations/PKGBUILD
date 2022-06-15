# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=albumentations
pkgname=python-albumentations
pkgver=1.2.0
pkgrel=1
pkgdesc='Fast image augmentation library and easy to use wrapper around other libraries'
arch=('any')
url='https://github.com/albumentations-team/albumentations'
license=('MIT')
depends=(
  python-imgaug
  python-numpy
  python-opencv
  python-pillow
  python-qudida
  python-tqdm
  python-yaml
)
makedepends=(
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/albumentations-team/albumentations/archive/${pkgver}.tar.gz")
sha512sums=('a9b8f9fb43b9cb9822e1a41e7e6b6b89bec728e7118cc8014d8c4db4a20056a4e514e874d17728e6da8d2e69566d6bf92edd0f29bf646f505a1783772cab7005')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
