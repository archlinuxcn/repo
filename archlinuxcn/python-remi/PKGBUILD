# Maintainer: Hu Butui <hot123tea123@gmail.com>

_pkgname=remi
pkgname=python-remi
pkgver=2022.7.27
pkgrel=3
pkgdesc='Cross-platform GUI library which renders in a web browser'
arch=('any')
url='https://github.com/dddomodossola/remi'
license=('Apache-2.0')
depends=(
  python
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
optdepends=(
  'python-pywebview: for standalone app'
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/dddomodossola/remi/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('362375d60e4e460a88c9f2198a83ae7a6476a32987d2fc97154211be829331f5')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  rm -rf "${pkgdir}${site_packages}/test"
  install -dm755 "${pkgdir}/usr/share/doc/${pkgname}"
  mv -vf "examples" "${pkgdir}/usr/share/doc/${pkgname}"
}
# vim:set ts=2 sw=2 et:
