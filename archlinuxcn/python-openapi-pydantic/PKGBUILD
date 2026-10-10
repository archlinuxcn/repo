# Maintainer:  Vitalii Kuzhdin <vitaliikuzhdin@gmail.com>

_pypiname="openapi-pydantic"
pkgname="python-${_pypiname}"
pkgver=0.6.0
pkgrel=1
pkgdesc="Modern, type-safe OpenAPI schemas in Python using Pydantic 1.8+ and 2.x"
arch=(
  'any'
)
url="https://github.com/mike-oakley/${_pypiname}"
license=(
  'MIT'
)
depends=(
  'python>=3.9'
  'python-pydantic>=1.8'
  'python-pydantic-core'
)
makedepends=(
  'python-build'
  'python-hatchling>=1.26'
  'python-installer'
  'python-wheel'
)
checkdepends=(
  'python-pytest>=8.3.5'
  'python-openapi-spec-validator'
)
_pkgsrc="${url##*/}-${pkgver}"
source=(
  "${url}/archive/refs/tags/v${pkgver}/${_pkgsrc}.tar.gz"
)
sha256sums=('a8dc20ce271be8419e207605f29f957620f4e872f258b4550a4223afb76ca5a2')

build() {
  cd "${srcdir}/${_pkgsrc}"
  python -m build --wheel --no-isolation
}

check() {
  cd "${srcdir}/${_pkgsrc}"
  pytest
}

package() {
  local site_packages="$(python -c "import site; print(site.getsitepackages()[0])")"

  cd "${srcdir}/${_pkgsrc}"
  python -m installer --destdir="${pkgdir}" dist/*.whl

  install -vDm644 "README.md" -t "${pkgdir}/usr/share/doc/${pkgname}"

  install -vd "${pkgdir}/usr/share/licenses"
  ln -vsf "${site_packages}/${_pypiname//-/_}-${pkgver%%+r*}.dist-info/licenses" \
    "${pkgdir}/usr/share/licenses/${pkgname}"
}
