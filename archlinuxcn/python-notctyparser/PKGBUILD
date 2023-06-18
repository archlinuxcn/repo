# Maintainer: edward-p <edward at edward-p dot xyz>

_base=notctyparser
pkgname=python-${_base}
pkgdesc="A fork and extension of ctyparser."
pkgver=23.6.18
pkgrel=1
arch=(any)
url="https://github.com/mbridak/ctyparser"
license=(MIT)
depends=(python python-feedparser python-requests python-lxml)
makedepends=(python-build python-installer python-setuptools python-wheel)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('5bfd9bb2e3b84564465f6d642d7d955441ad6e01f82e5457e9c70c1be3144bb3da5efe1cddae6620a71ff3bab53ef6ec8eb41c51f1c76b136b888984682c31a7')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
