# Maintainer: Butui Hu <hot123tea123@gmail.com>
# Contributor: Mohammad Hossein Sekhavat <sekhavat17@gmail.com>

_pkgname=streamlit
pkgname=python-streamlit
pkgver=1.12.0
pkgrel=1
pkgdesc='The fastest way to build data apps in Python'
arch=('any')
url='https://streamlit.io'
license=('Apache')
depends=(
  python-altair
  python-astor
  python-attrs
  python-base58
  python-blinker
  python-cachetools
  python-click
  python-dateutil
  python-gitpython
  python-numpy
  python-packaging
  python-pandas
  python-pillow
  python-protobuf
  python-pyarrow
  python-pydeck
  python-pympler
  python-requests
  python-toml
  python-tornado
  python-tzlocal
  python-validators
  python-watchdog
  semver
)
makedepends=(
  python-pipenv
  python-setuptools
)

source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz"
)
sha512sums=('343b9eedf967234e5dcab3b4d79ebd2e420e767aaa1666a08cf78deef259ee44d360fe49ce8c28f39563c43a2883a1e178f3aaf37908991098c7e540b1b6e87d')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=0 --skip-build
  rm -vf "${pkgdir}/usr/bin/streamlit.cmd"
}
# vim:set ts=2 sw=2 et:
