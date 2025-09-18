# Maintainer: Claudia Pellegrino <aur ät cpellegrino.de>

pkgname=python-minerva-git
_gitpkgname=minerva
pkgver=r137.b9fb6d8
pkgrel=1
pkgdesc='32-bit RISC-V soft processor'
arch=('any')
url='https://github.com/minerva-cpu/minerva'
license=('BSD-3-Clause')
depends=(
  'python'
  'python-amaranth'
  'python-amaranth-soc'
)
makedepends=(
  'git'
  'python-build'
  'python-installer'
  'python-pdm-backend'
  'python-wheel'
)
checkdepends=(
  'python-pdm'
  'symbiyosys'
  'yices'
)
provides=("python-minerva=${pkgver}")
conflicts=('python-minerva')

source=(
  "${_gitpkgname}::git+https://github.com/minerva-cpu/minerva.git"
  "pipeline-diagram.png::https://docs.google.com/drawings/d/e/2PACX-1vTMkQc8ZJoiJ2AOeFGMkK0QTNx1hSG5wDrG5seLdJ3i61E4ag7wH7VFey44qhvuXotvOKxOw-mFS-VE/pub?w=850&h=761"
)

sha512sums=(
  'SKIP'
  'SKIP'
)

pkgver() {
  printf "r%s.%s" \
    "$(git -C "${_gitpkgname}" rev-list --count HEAD)" \
    "$(git -C "${_gitpkgname}" rev-parse --short HEAD)"
}

prepare() {
  cd "${_gitpkgname}"

  echo >&2 'Patching tests to use symbiyosys instead of yowasp-yosys'
  sed -i -e 's/yowasp-sby/sby/' minerva/test/utils.py

  echo >&2 'Adjusting image links'
  sed -i -e 's/\(!\[Pipeline Diagram Image\]\)([^)]*)/\1(.\/pipeline-diagram.png)/' \
    README.md
}

build() {
  cd "${_gitpkgname}"
  python -m build --wheel --no-isolation
}

check() {
  cd "${_gitpkgname}"
  PDM_USE_VENV=false SBY=sby YOSYS=yosys python -m unittest discover -v
}

package() {
  cd "${_gitpkgname}"

  echo >&2 'Packaging the wheel'
  python -I -m installer --destdir="${pkgdir}" dist/*.whl

  echo >&2 'Packaging the documentation'
  install -D -m 644 -t "${pkgdir}/usr/share/doc/${pkgname}" \
    README.md ../pipeline-diagram.png

  echo >&2 'Packaging the license'
  install -D -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
    LICENSE.txt
}
