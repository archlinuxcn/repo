# Maintainer: txtsd <aur.archlinux@ihavea.quest>

pkgname=python-wassima
_pkgname="${pkgname/python-/}"
pkgver=2.1.0
pkgrel=1
pkgdesc='No more certifi! System trust store at hand. In Pure Python.'
arch=('any')
url='https://github.com/jawah/wassima'
license=('MIT')
depends=(python)
makedepends=(
  python-build
  python-hatchling
  python-installer
  python-wheel
)
options=(!debug)
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('1f22ad95e6553e8ae8d29b708b89d3f2be8fbad9710b3f7cbe6229de4ea36a99')

build() {
  cd "${_pkgname}-${pkgver}"

  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"

  python -m installer --destdir="${pkgdir}" dist/*.whl

  install -Dm0644 -t "${pkgdir}/usr/share/licenses/${pkgname}/" LICENSE
  install -Dm0644 -t "${pkgdir}/usr/share/doc/${pkgname}/" {CHANGELOG,README,SECURITY}.md NOTICE
}
