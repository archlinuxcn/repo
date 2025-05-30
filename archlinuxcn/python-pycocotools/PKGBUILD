# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pycocotools
_pkgname=pycocotools
pkgver=2.0.9
pkgrel=1
pkgdesc='Official APIs for the MS-COCO dataset'
arch=(x86_64)
url='https://pypi.org/project/pycocotools'
license=('BSD-2-Clause')
depends=(
  glibc
  python-matplotlib
  python-numpy
)
makedepends=(
  cython
  python-build
  python-installer
  python-setuptools
  python-wheel
)

source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz"
        "LICENSE::https://github.com/cocodataset/cocoapi/raw/master/license.txt")
sha512sums=('21fec6bedca09ec15895f73331533c033010ea7ad3d5b2df6a6112ba0bb93d8bb39148df8254ac4750d06f0083d44a2d8d75ca0e311782ffc78641b3ec945091'
            '5fe64df67e41aa3fa97db466cedfbf659c308db1917d46396721e2d05146083323ef35f18b45e792f2bff70919449fc74394518d60c8ccf63979ae20ceb21595')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation --skip-dependency-check
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 "${srcdir}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
