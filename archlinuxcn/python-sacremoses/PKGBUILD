# Maintainer: Butui Hu <hot123tea123@gmail.com>
# Contributor: Tommy Li <ttoo74@gmail.com>

_pkgname=sacremoses
pkgname=python-sacremoses
pkgver=0.2.0
pkgrel=1
pkgdesc='Python port of Moses tokenizer, truecaser and normalizer'
arch=('any')
url='https://github.com/alvations/sacremoses'
license=(MIT)
depends=(
  python-click
  python-joblib
  python-regex
  python-six
  python-tqdm
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha512sums=('3f0b261b83af61fb8e16744af240d60ecf7708ee8cbd365a43e557d81021804caab98bb4df4b24ff8e2300a6101d6453209b553e13e7d107f75cbd614ae9710f')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 "LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
