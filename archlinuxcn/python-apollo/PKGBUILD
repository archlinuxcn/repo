# Maintainer: Claudia Pellegrino <aur ät cpellegrino.de>

pkgname=python-apollo
_gitpkgname=apollo
pkgver=1.1.1
pkgrel=1
pkgdesc='Microcontroller-based FPGA/JTAG programmer'
arch=('any')
url='https://github.com/greatscottgadgets/apollo'
license=('BSD-3-Clause')
depends=(
  'python'
  'python-deprecation'
  'python-prompt_toolkit'
  'python-pyusb'
  'python-pyvcd'
  'python-pyxdg'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-pyproject-patcher'
  'python-setuptools'
  'python-wheel'
)
checkdepends=(
  'python-pytest'
)
optdepends=(
  'python-amaranth: for flashing'
  'python-luna-usb: to use the flash-fast subcommand'
  'python-pyserial: to connect to an integrated logic analyzer'
  'python-usb-protocol: for flashing'
)

source=(
  "${_gitpkgname}-${pkgver}.tar.gz::https://github.com/greatscottgadgets/apollo/archive/v${pkgver}.tar.gz"
)

sha512sums=('67475167f379a988543b5e2740f7de6fdc6dc86daa6f2cf4687224609bae5db7555a26d75b5d7bff721c3809476962a0c3bc084f0e96e437188e123c3d2226d8')

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
  python -m build --wheel --no-isolation
}

check() {
  cd "${_gitpkgname}-${pkgver}"
  local _site_packages LUNA_USB_IDS PYTHONPATH
  python -m installer --destdir=tmp_install dist/*.whl

  _site_packages="$(python -c 'import site; print(site.getsitepackages()[0])')"
  PYTHONPATH="${PWD}/tmp_install/${_site_packages}"
  export PYTHONPATH

  echo >&2 'Testing the executable'
  "tmp_install/usr/bin/${_gitpkgname}" info >actual.txt 2>&1 || true
  if ! grep -qF "Apollo version: ${pkgver}" actual.txt; then
    printf >&2 '%s\n' 'Unexpected test output:' '==='
    cat >&2 actual.txt
    printf >&2 '\n%s\n' '==='
    exit 1
  fi
}

package() {
  cd "${_gitpkgname}-${pkgver}"

  echo >&2 'Packaging the wheel'
  python -I -m installer --destdir="${pkgdir}" dist/*.whl

  echo >&2 'Packaging udev rules'
  install -D -m 644 -t "${pkgdir}/usr/lib/udev/rules.d" \
    misc/*.rules

  echo >&2 'Packaging the documentation'
  install -D -m 644 -t "${pkgdir}/usr/share/doc/${pkgname}" \
    README.md

  echo >&2 'Packaging the license'
  install -D -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
    LICENSE
}
