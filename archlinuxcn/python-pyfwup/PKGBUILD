# Maintainer: Claudia Pellegrino <aur ät cpellegrino.de>

pkgname=python-pyfwup
_gitpkgname=pyfwup
pkgver=0.5.3
pkgrel=1
pkgdesc='Python Firmware Upgrader, a DFU (and similar) utility for Python'
arch=('any')
url='https://github.com/greatscottgadgets/pyfwup'
license=('BSD-3-Clause')
depends=(
  'python'
  'python-pyusb'
  'python-tqdm'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-pyproject-patcher'
  'python-setuptools'
  'python-wheel'
)

source=(
  "${_gitpkgname}-${pkgver}.tar.gz::https://github.com/greatscottgadgets/pyfwup/archive/${pkgver}.tar.gz"
)

sha512sums=('f72460be5352f49606e31750fa4c5a836498bf204dc76346fc6ddaba2b3fd4158c0c536425b7be36878a4e1699d772df869f724b3a9edc034d14f9bbd2eb04e8')

prepare() {
  cd "${_gitpkgname}-${pkgver}"

  echo >&2 'Pinning version number'
  export pkgver
  python << 'EOF'
from pyproject_patcher import patch_in_place
with patch_in_place('pyproject.toml') as toml:
    toml.set_project_version_from_env('pkgver')
    toml.tools.setuptools_git_versioning.remove()
EOF
}

build() {
  cd "${_gitpkgname}-${pkgver}"
  echo >&2 'Building wheel'
  python -m build --wheel --no-isolation
}

package() {
  cd "${_gitpkgname}-${pkgver}"

  echo >&2 'Packaging the wheel'
  python -I -m installer --destdir="${pkgdir}" dist/*.whl

  echo >&2 'Packaging the documentation'
  install -D -m 644 -t "${pkgdir}/usr/share/doc/${pkgname}" \
    README.md

  echo >&2 'Packaging the license'
  install -D -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
    LICENSE
}
