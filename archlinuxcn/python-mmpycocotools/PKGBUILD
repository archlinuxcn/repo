# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-mmpycocotools
_pkgname=mmpycocotools
pkgver=12.0.2
pkgrel=2
pkgdesc='Official APIs for the MS-COCO dataset (openmm lab fork)'
arch=(x86_64)
url='https://pypi.org/project/mmpycocotools'
license=(BSD)
depends=(
  python-matplotlib
  python-numpy
)
makedepends=(
  cython
  python-setuptools
)
provides=(python-pycocotools)
conflicts=(python-pycocotools)
replaces=(python-pycocotools-openmm-git)

source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz
"
        "https://github.com/open-mmlab/cocoapi/raw/master/license.txt"
)
sha512sums=('34a866568d3b1dcd5d6b24255ce73171a9cd3df19308532062d664c70bd562f8d314298adc524fa8474813cc2b1b84e0288cc781d7753f648403d7c52de4a8f1'
            'b0dc48c4d0fa9eaa101bf94dd75df4b23a9281ba714b0c1f01204d2d48c6f1de14cbe093590b16ef614168621146c9f708f6af2543561a56c76c81b66113c435')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 "${srcdir}/license.txt" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
