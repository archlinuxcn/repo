# Maintainer:  Noor Christensen <archlinux_AT_technopragmatics_DOT_org>
# Maintainer:  Vitalii Kuzhdin <vitaliikuzhdin@gmail.com>

_name="textual-autocomplete"
pkgname="python-${_name}"
pkgver=4.0.6
pkgrel=1
pkgdesc="Easily add autocomplete dropdowns to your Textual apps"
arch=('any')
url="https://github.com/darrenburns/${_name}"
license=('MIT')
depends=(
  'python>=3.9'
  'python-rich'
  'python-textual>=2'
  # 'python-typing_extensions>=4.5'
)
makedepends=(
  'python-build'
  'python-hatchling'
  'python-installer'
)
# checkdepends=(
#   'python-pytest>=8.3.5'
#   'python-pytest-asyncio>=0.24'
#   'python-pytest-textual-snapshot>=1.1'
#   'python-pytest-xdist>=3.6.1'
# )
_pkgsrc="${_name//-/_}-${pkgver}"
source=("${_pkgsrc}.tar.gz::https://files.pythonhosted.org/packages/source/${_name::1}/${_name//-/_}/${_pkgsrc}.tar.gz")
sha256sums=('2ba2f0d767be4480ecacb3e4b130cf07340e033c3500fc424fed9125d27a4586')

build() {
  cd "${srcdir}/${_pkgsrc}"
  python -m build --wheel --no-isolation
}

# check() {
#   cd "${srcdir}/${_pkgsrc}"
#   python -m venv --system-site-packages test-env
#   test-env/bin/python -m installer dist/*.whl
#   test-env/bin/python -P -m pytest
# }

package() {
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")

  cd "${srcdir}/${_pkgsrc}"
  python -m installer --destdir="${pkgdir}" dist/*.whl

  install -vDm644 "README.md" "${pkgdir}/usr/share/doc/${pkgname}/README.md"

  install -vd "${pkgdir}/usr/share/licenses/${pkgname}"
  ln -vsf "${site_packages}/${_pkgsrc}.dist-info/licenses/LICENSE" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
