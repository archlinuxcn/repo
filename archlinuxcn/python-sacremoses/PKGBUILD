# Maintainer: Butui Hu <hot123tea123@gmail.com>
# Contributor: Tommy Li <ttoo74@gmail.com>

_pkgname=sacremoses
pkgname=python-sacremoses
pkgver=0.1.1
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
sha512sums=('c000c8bed89c1417ee8004bd0750a6917f51a18e4b39f271ba467922f2bd2ce3460f6ad83c46f08de06997446fea3e380a5502801f0937b849939ad714d42a16')

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
