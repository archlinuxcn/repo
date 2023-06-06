# Maintainer: edward-p <edward at edward-p dot xyz>

_base=notctyparser
pkgname=python-${_base}
pkgdesc="A fork and extension of ctyparser."
pkgver=23.6.4
pkgrel=1
arch=(any)
url="https://github.com/mbridak/ctyparser"
license=(MIT)
depends=(python python-feedparser python-requests python-lxml)
makedepends=(python-build python-installer python-setuptools python-wheel)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('d2f7237f2d92baed5220e53a96d8d526baf7ed6274cdc4ef53e7767e09773d1c6c8a3384f19b155a4ef96cdb3c8f61558859b981995eb51ad8d724b3b4a5a9d6')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
