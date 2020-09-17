# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmlvis
pkgname=python-mmlvis
pkgver=10.5.3
pkgrel=2
pkgdesc='Python API for LVIS Dataset (openmm lab fork)'
arch=('any')
url='https://pypi.org/project/mmlvis'
license=(BSD)
depends=(
  opencv
  python-cycler
  python-dateutil
  python-kiwisolver
  python-matplotlib
  python-numpy
  python-pyparsing
  python-mmpycocotools
  python-six
)
makedepends=(
  python-pip
)
provides=(python-lvis)
conflicts=(python-lvis)
replaces=(python-lvis-openmm-git)

source=("https://files.pythonhosted.org/packages/py3/${_pkgname::1}/${_pkgname}/${_pkgname/-/_}-${pkgver}-py3-none-any.whl"
        "https://github.com/open-mmlab/cocoapi/raw/master/license.txt"
)
sha512sums=('02c86f7b002d6e47ae4e497c0b78dc8e3496e04c8cfd3c7cf605d7c72da455e04051d5e8cad0cdd7fa23fc55535420731cabaaf33c584335a8b6ff20c0a2a52e'
            'b0dc48c4d0fa9eaa101bf94dd75df4b23a9281ba714b0c1f01204d2d48c6f1de14cbe093590b16ef614168621146c9f708f6af2543561a56c76c81b66113c435')

package() {
  PIP_CONFIG_FILE=/dev/null pip install --isolated --root="${pkgdir}" --ignore-installed --no-deps *.whl
  python -O -m compileall "${pkgdir}"
  install -Dm644 "${srcdir}/license.txt" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
