# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pycocotools
_pkgname=pycocotools
pkgver=2.0.5
pkgrel=1
pkgdesc='Official APIs for the MS-COCO dataset'
arch=(x86_64)
url='https://pypi.org/project/pycocotools'
license=(BSD)
depends=(
  python-matplotlib
  python-numpy
)
makedepends=(
  cython
  python-setuptools
)

source=("${pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz"
        "LICENSE::https://github.com/cocodataset/cocoapi/raw/master/license.txt")
sha512sums=('523036d736764f5f34419f2ec2f59c43a59473e84a2812284ad61658e7461a22644f5621ae346dce6e356ed6b04a0682adfb7800fd55bb943488d1099ab99e77'
            '5fe64df67e41aa3fa97db466cedfbf659c308db1917d46396721e2d05146083323ef35f18b45e792f2bff70919449fc74394518d60c8ccf63979ae20ceb21595')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 "${srcdir}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
