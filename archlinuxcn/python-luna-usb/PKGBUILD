# Maintainer: Claudia Pellegrino <aur ät cpellegrino.de>

pkgname=python-luna-usb
_gitpkgname=luna
pkgver=0.2.3
pkgrel=1
pkgdesc='Amaranth HDL framework for monitoring, hacking, and developing USB devices'
arch=('any')
url='https://github.com/greatscottgadgets/luna'
license=('BSD-3-Clause')
depends=(
  'python'
  'python-amaranth>=0.5'
  'python-apollo'
  'python-pyserial'
  'python-pyusb'
  'python-pyvcd'
  'python-usb-protocol'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-jschon'
  'python-pyproject-patcher'
  'python-setuptools'
  'python-sphinx'
  'python-sphinx_rtd_theme'
  'python-wheel'
)
optdepends=(
  'python-cynthion: connect to Cynthion hardware'
  'python-libusb1: to use the bulk_speed_test applet'
  'python-luna-boards: connect to Luna boards'
  'python-prompt_toolkit: to use the included applets'
)

source=(
  "${_gitpkgname}-${pkgver}.tar.gz::https://github.com/greatscottgadgets/luna/archive/${pkgver}.tar.gz"
)

sha512sums=('5e3d33fe283ee7b9a8982b9a75bc85d75cf92bbd08df092101bb4e26a90105eb56a1449815cc7ff31f4445733992d7224ffbd5891da1748735aaa61a6a6d951f')

prepare() {
  cd "${_gitpkgname}-${pkgver}"

  echo >&2 'Removing unneeded files'
  find examples -name '.*' -exec rm -fv '{}' +

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

  export PYTHONPATH=.

  echo >&2 'Generating man page'
  sphinx-build -aqEW -b man docs docs/build/man

  echo >&2 'Generating HTML documentation'
  sphinx-build -aqEW -b singlehtml docs docs/build/singlehtml
}

check() {
  cd "${_gitpkgname}-${pkgver}"
  python -m unittest discover -v
}

package() {
  cd "${_gitpkgname}-${pkgver}"

  echo >&2 'Packaging the wheel'
  python -I -m installer --destdir="${pkgdir}" dist/*.whl

  echo >&2 'Packaging udev rules'
  install -D -m 644 -t "${pkgdir}/usr/lib/udev/rules.d" \
    contrib/*.rules

  echo >&2 'Packaging the documentation'
  install -D -m 644 -t "${pkgdir}/usr/share/doc/${pkgname}" \
    README.md
  install -D -m 644 -t "${pkgdir}/usr/share/doc/${pkgname}/gtkwave" \
    contrib/usb3-gtkwave.txt
  cp -R --preserve=mode -t "${pkgdir}/usr/share/doc/${pkgname}" \
    docs/build/singlehtml/{index.html,_images,_static}
  install -D -m 644 -t "${pkgdir}/usr/share/man/man1" \
    docs/build/man/*.1

  echo >&2 'Packaging applets and examples'
  mkdir -p "${pkgdir}/usr/share/${pkgname}"
  cp -R --preserve=mode -t "${pkgdir}/usr/share/${pkgname}" \
    applets examples

  echo >&2 'Packaging the license'
  install -D -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
    LICENSE
}
