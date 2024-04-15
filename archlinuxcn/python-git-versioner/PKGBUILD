# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=__version__
pkgname=python-git-versioner
pkgver=7.1
pkgrel=1
pkgdesc="Manage current / next version for project"
arch=(any)
url="https://gitlab.com/alelec/${_base}"
license=(MIT)
depends=(python-setuptools)
makedepends=(python-build python-installer python-wheel)
source=(${url}/-/archive/v${pkgver}/${_base}-v${pkgver}.tar.gz)
sha512sums=('34b6fb4ad5bcec3c3ba78451c6c9716b330aca11e4752daa8ddaad6c1fbd1ddc9f263e24263bb02e96e28df656cf9c04f31cc67ac6edd8d025f82a7a77b54f46')

build() {
  cd ${_base}-v${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-v${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
