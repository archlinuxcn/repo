# Maintainer: edward-p <edward at edward-p dot xyz>

_base=notctyparser
pkgname=python-${_base}
pkgdesc="A fork and extension of ctyparser."
pkgver=26.8.31
pkgrel=1
arch=(any)
url="https://github.com/mbridak/ctyparser"
license=(MIT)
depends=(python python-feedparser python-requests python-lxml)
makedepends=(python-build python-installer python-setuptools python-wheel)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('3fec15a54798ec4f5eb4cffa7fc8714b1d174a8568d3af29a0ecb6bbb45b2c7eb2208544cd856a4d815d75a687dfb2eb4811b6c1185e1aab8aff9693fb17311b')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/docs/"
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
