# Maintainer: Butui Hu <hot123tea123@gmail.com>
# Contributor: pingplug < aur at pingplug dot me >

_pkgname=openslide-python
pkgname=python-openslide
pkgver=1.4.3
pkgrel=1
pkgdesc='Python bindings to OpenSlide'
arch=('x86_64')
url='https://github.com/openslide/openslide-python'
license=('LGPL')
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
checkdepends=(python-pytest)
depends=(
  openslide
  python-pillow
)
source=(
  "${_pkgname}-${pkgver}.tar.gz::https://github.com/openslide/openslide-python/archive/v${pkgver}.tar.gz"
)
sha256sums=('2b56987a4b46cfd69e4e7a033949a1c13863db0e578568b8cb488ec9ddf27cb2')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

check() {
  local python_version=$(python -c 'import sys; print("".join(map(str, sys.version_info[:2])))')
  cd "${_pkgname}-${pkgver}"
  PYTHONPATH="$PWD/build/lib.linux-$CARCH-cpython-${python_version}" pytest -v
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
# vim:set ts=2 sw=2 et:
