# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-mmpycocotools
_pkgname=mmpycocotools
pkgver=12.0.3
pkgrel=5
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
  python-build
  python-installer
  python-setuptools
  python-wheel
)
provides=(python-pycocotools)
conflicts=(python-pycocotools)
replaces=(python-pycocotools-openmm-git)

source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz"
        "https://github.com/open-mmlab/cocoapi/raw/master/license.txt"
)
sha512sums=('8eb699757531edbb689f28895d0613d1f7bea88a6a6fadb4d4d30021ba7af8bd9e72f307c635746388b67817a6149b14fd82d1b03a84ca77adade4c4bfa77281'
            'b0dc48c4d0fa9eaa101bf94dd75df4b23a9281ba714b0c1f01204d2d48c6f1de14cbe093590b16ef614168621146c9f708f6af2543561a56c76c81b66113c435')

prepare() {
  # fix https://github.com/open-mmlab/cocoapi/issues/29
  sed -i "s,np.float,float,g" "${_pkgname}-${pkgver}/pycocotools/cocoeval.py"
}

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 "${srcdir}/license.txt" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
