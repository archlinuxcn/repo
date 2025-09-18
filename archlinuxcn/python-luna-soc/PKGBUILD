# Maintainer: Claudia Pellegrino <aur ät cpellegrino.de>

pkgname=python-luna-soc
_gitpkgname=luna-soc
pkgver=0.3.2
pkgrel=1
pkgdesc='Amaranth HDL libary for building USB-capable SoC designs'
arch=('any')
url='https://github.com/greatscottgadgets/luna-soc'
license=('BSD-3-Clause')
depends=(
  'python'
  'python-amaranth>=0.5'

  # Work around undeclared transitive dependency of python-amaranth
  # See also: https://aur.archlinux.org/packages/python-amaranth#comment-1016100
  'python-jschon'

  'python-luna-usb>=0.2'
  'python-pyserial'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-pyproject-patcher'
  'python-recommonmark'
  'python-setuptools'
  'python-sphinx'
  'python-sphinx_rtd_theme'
  'python-sphinxcontrib-apidoc'
  'python-wheel'
)
checkdepends=('python-apollo')
optdepends=(
  'python-minerva: to implement SoC designs using a Minerva RISC-V CPU'
)

source=(
  "${_gitpkgname}-${pkgver}.tar.gz::https://github.com/greatscottgadgets/luna-soc/archive/${pkgver}.tar.gz"
)

sha512sums=('aaaa528e436dc03c8fcb8e4e9e226d02d50f1c333bc3bd64b43873a7a852c75a8b40c6da7175271f86063c1b1456e3ed5658b297206ed2a0899bacd143d9442c')

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

  echo >&2 'Generating documentation'
  _site_packages="$(python -c 'import site; print(site.getsitepackages()[0])')"
  python -m installer --destdir=tmp_install dist/*.whl
  PYTHONPATH="${PWD}/tmp_install/${_site_packages}" \
    make -C docs singlehtml
}

check() {
  cd "${_gitpkgname}-${pkgver}"
  local LUNA_USB_IDS

  # Do not use real hardware if connected at check time
  export LUNA_USB_IDS='0xffff:0xffff'

  echo >&2 'Smoke testing the built-in CLI'
  python >actual.txt 2>&1 << 'EOF' || true
from apollo_fpga import ApolloDebugger
import luna_soc
luna_soc.top_level_cli(ApolloDebugger)
EOF
  if ! grep -qF 'apollo_fpga.DebuggerNotFound' actual.txt; then
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

  echo >&2 'Packaging the documentation'
  install -D -m 644 -t "${pkgdir}/usr/share/doc/${pkgname}" \
    README.md
  cp -R --preserve=mode -t "${pkgdir}/usr/share/doc/${pkgname}" \
    docs/build/singlehtml/{index.html,_images,_static}

  echo >&2 'Packaging examples'
  mkdir -p "${pkgdir}/usr/share/${pkgname}"
  cp -R --preserve=mode -t "${pkgdir}/usr/share/${pkgname}" \
    examples

  echo >&2 'Packaging the license'
  install -D -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
    LICENSE.txt
}
