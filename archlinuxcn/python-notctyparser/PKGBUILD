# Maintainer: edward-p <edward at edward-p dot xyz>

_base=notctyparser
pkgname=python-${_base}
pkgdesc="A fork and extension of ctyparser."
pkgver=23.6.21
pkgrel=1
arch=(any)
url="https://github.com/mbridak/ctyparser"
license=(MIT)
depends=(python python-feedparser python-requests python-lxml)
makedepends=(python-build python-installer python-setuptools python-wheel)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('80ec493e6952c66b539df29e4d80a5ed1e1849fb6a8b9b673df4bc66de0716ec9d3e830d2d8f5c866ca34cde2e6e7b9598cbbdc30a7be66893b7865cc2661df1')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
