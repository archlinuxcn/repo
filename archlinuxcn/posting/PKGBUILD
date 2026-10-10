# Maintainer:  Noor Christensen <archlinux_AT_technopragmatics_DOT_org>
# Maintainer:  Vitalii Kuzhdin <vitaliikuzhdin@gmail.com>

pkgname="posting"
pkgver=2.11.2
pkgrel=1
pkgdesc="The modern API client that lives in your terminal"
arch=(
  'any'
)
url="https://github.com/darrenburns/${pkgname}"
license=(
  'MIT'
)
depends=(
  'python>=3.11'
  'python-click>=8.1.7'
  'python-xdg-base-dirs>=6.0.1'
  'python-click-default-group>=1.2.4'
  'python-httpx>=0.28.1'
  'python-openapi-pydantic>=0.5.0'
  'python-pyperclip>=1.9.0'
  'python-pydantic>=2.9.2'
  'python-yaml>=6.0.2'
  'python-pydantic-settings>=2.4.0'
  'python-dotenv>=1.0.1'
  'python-watchfiles>=0.24.0'
  'python-textual>=6.1.0'
  'python-textual-autocomplete>=4.0.6'

  # 'python-linkify-it-py'
  'python-rich'
  'python-typing_extensions'
)
makedepends=(
  'python-build'
  'python-hatchling'
  'python-installer'

  # 'mkdocs-material>=9.5.30'
)
# checkdepends=(
#   'python-pytest>=8.3.1'
#   'python-pytest-xdist>=3.6.1'
# )
provides=(
  "python-${pkgname}=${pkgver}"
)
conflicts=(
  "python-${pkgname}"
)
_pkgsrc="${pkgname}-${pkgver}"
source=(
  "${url}/archive/refs/tags/${pkgver}/${_pkgsrc}.tar.gz"
)
sha256sums=('64f79be3b3d04c8a9653497dc03b9c04436a7db54098f14bb4c2daa1f6626e1f')

build() {
  cd "${srcdir}/${_pkgsrc}"
  python -m build --wheel --no-isolation
}

# check() {
#   cd "${srcdir}/${_pkgsrc}"
#   python -m venv --system-site-packages test-env
#   test-env/bin/python -m installer dist/*.whl
#   test-env/bin/python -P -m pytest tests/ -m "not serial"
# }

package() {
  local site_packages="$(python -c "import site; print(site.getsitepackages()[0])")"

  cd "${srcdir}/${_pkgsrc}"
  python -m installer --destdir="${pkgdir}" dist/*.whl

  install -vDm644 "README.md" -t "${pkgdir}/usr/share/doc/${pkgname}"

  install -vd "${pkgdir}/usr/share/licenses"
  ln -vsf "${site_packages}/${_pkgsrc}.dist-info/licenses" \
    "${pkgdir}/usr/share/licenses/${pkgname}"
}
