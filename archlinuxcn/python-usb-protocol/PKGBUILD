# Maintainer: Claudia Pellegrino <aur ät cpellegrino.de>

pkgname=python-usb-protocol
pkgver=0.9.2
pkgrel=1
pkgdesc='Utilities, data structures, constants, parsers, and tools for working with USB data'
arch=('any')
url='https://github.com/greatscottgadgets/python-usb-protocol'
license=('BSD-3-Clause')
depends=(
  'python'
  'python-construct'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-pyproject-patcher'
  'python-recommonmark'
  'python-setuptools'
  'python-sphinx'
  'python-sphinxcontrib-apidoc'
  'python-sphinx_rtd_theme'
  'python-wheel'
)

source=(
  "${pkgname}-${pkgver}.tar.gz::https://github.com/greatscottgadgets/python-usb-protocol/archive/${pkgver}.tar.gz"
)

sha512sums=('187c35c2cd7ae7ac0f246c8c8eba794226718d1c4374cbb605c9645dc1a1ff353feaf8be283ce4ea6d9a3469e2cc022dfd368fe63266ef4ed323181925bbe64f')

prepare() {
  cd "${pkgname}-${pkgver}"

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
  local _site_packages
  cd "${pkgname}-${pkgver}"
  echo >&2 'Building wheel'
  python -m build --wheel --no-isolation

  echo >&2 'Generating documentation'
  _site_packages="$(python -c 'import site; print(site.getsitepackages()[0])')"
  python -m installer --destdir=tmp_install dist/*.whl
  PYTHONPATH="${PWD}/tmp_install/${_site_packages}" \
    make -C docs singlehtml
}

check() {
  cd "${pkgname}-${pkgver}"
  python -m unittest discover -v
}

package() {
  cd "${pkgname}-${pkgver}"

  echo >&2 'Packaging the wheel'
  python -I -m installer --destdir="${pkgdir}" dist/*.whl

  echo >&2 'Packaging the documentation'
  install -D -m 644 -t "${pkgdir}/usr/share/doc/${pkgname}" \
    README.md
  cp -R --preserve=mode -t "${pkgdir}/usr/share/doc/${pkgname}" \
    docs/build/singlehtml/{index.html,_static}

  echo >&2 'Packaging the examples'
  install -D -m 644 -t "${pkgdir}/usr/share/${pkgname}/examples" \
    examples/*

  echo >&2 'Packaging the license'
  install -D -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
    LICENSE.txt
}
