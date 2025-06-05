# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pycocotools
_pkgname=pycocotools
pkgver=2.0.10
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
sha512sums=('43722c92930441501c8b3aa8c2ca0dfef26397246f35d341212c3e3b0c284412f91e66c42d723a785a98cbf15b7dd4a4e5583283bff4e523570f0f114209d8ba'
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
