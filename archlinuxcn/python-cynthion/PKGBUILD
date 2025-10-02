# Maintainer: Claudia Pellegrino <aur ät cpellegrino.de>

pkgname=python-cynthion
_gitpkgname=cynthion
pkgver=0.2.4
pkgrel=1
pkgdesc='Python package and utilities for the Great Scott Gadgets Cynthion USB Test Instrument'
arch=('any')
url='https://github.com/greatscottgadgets/cynthion'
license=('BSD-3-Clause')
depends=(
  "cynthion-firmware=${pkgver}"
  'python'
  'python-amaranth>=0.5'
  'python-apollo'
  'python-luna-usb>=0.2'
  'python-luna-soc>=0.3'
  'python-pyfwup'
  'python-pygreat'
  'python-pyusb'
  'python-tomli'
  'python-tqdm'
  'python-usb-protocol'
)
makedepends=(
  'git'
  'python-build'
  'python-installer'
  'python-pyproject-patcher'
  'python-setuptools'
  'python-sphinx'
  'python-sphinx_rtd_theme'
  'python-sphinx-inline-tabs'
  'python-wheel'
)
optdepends=(
  'python-facedancer: to run the included examples'
)

source=(
  "${_gitpkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz"
  'archlinux-managed-udev-rules.patch'
)

sha512sums=('e37efbd54cf58c1ee65f76096497ea9770e36d3d847e32d54fb5765e5a4e29b39d491b25577d1c29820c75da280e10227bf0a01059a600bfc35f28724150524f'
            '45d3b73f3651485177b43ffb2d413a7a008f01550dcff7973e6581afb337b6b37beda50ee8499a632754e791734186ec647eb48bea8a3efb2899844bac40fd0b')

prepare() {
  cd "${_gitpkgname}-${pkgver}"

  echo >&2 'Pinning version number'
  export pkgver
  python << 'EOF'
from pyproject_patcher import patch_in_place
with patch_in_place('cynthion/python/pyproject.toml') as toml:
    toml.set_project_version_from_env('pkgver')
    toml.tools.setuptools_git_versioning.remove()
EOF

  echo >&2 'Patching the setup subcommand so it knows about pacman-managed files'
  patch -p1 < ../archlinux-managed-udev-rules.patch
}

build() {
  cd "${_gitpkgname}-${pkgver}"

  echo >&2 'Building wheel'
  python -m build --wheel --no-isolation cynthion/python

  echo >&2 'Generating documentation'
  make -C docs singlehtml
}

check() {
  cd "${_gitpkgname}-${pkgver}"
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer cynthion/python/dist/*.whl

  echo >&2 'Running unit tests'
  test-env/bin/python -m unittest discover -v cynthion/python/tests
}

package() {
  cd "${_gitpkgname}-${pkgver}"
  local _site_packages

  echo >&2 'Packaging the wheel'
  python -I -m installer --destdir="${pkgdir}" cynthion/python/dist/*.whl

  echo >&2 'Symlinking binaries and bitstreams'
  _site_packages="$(
    python -c 'import site; print(site.getsitepackages()[0])'
  )"
  mkdir -p "${pkgdir}/${_site_packages}/cynthion/assets"
  find /usr/lib/cynthion-firmware -maxdepth 1 \
    '-(' -name '*.bin' -o -name 'CynthionPlatform*' '-)' -exec \
    ln -fnsv '{}' "${pkgdir}/${_site_packages}/cynthion/assets/" ';'

  echo >&2 'Packaging udev rules'
  install -D -m 644 -t "${pkgdir}/usr/lib/udev/rules.d" \
    cynthion/python/assets/*.rules

  echo >&2 'Packaging the documentation'
  install -D -m 644 -t "${pkgdir}/usr/share/doc/${pkgname}" \
    README.md
  cp -R --preserve=mode -t "${pkgdir}/usr/share/doc/${pkgname}" \
    docs/build/singlehtml/{index.html,_images,_static}

  echo >&2 'Packaging the examples'
  mkdir -p "${pkgdir}/usr/share/${pkgname}"
  cp -R --preserve=mode -t "${pkgdir}/usr/share/${pkgname}" \
    cynthion/python/examples

  echo >&2 'Packaging the license'
  install -D -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
    LICENSE.txt
}
