# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=streamlit-webrtc
pkgname=python-streamlit-webrtc
pkgver=0.35.1
pkgrel=1
pkgdesc='Real-time video and audio streams over the network, with Streamlit'
arch=('any')
url='https://github.com/whitphx/streamlit-webrtc'
license=('MIT')
depends=(
  python-aiortc
  python-streamlit
)
makedepends=(
  python-setuptools
)

source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha512sums=('17633e83fb3135f2a9929f95699c3dc2cf3f1689255df8ee923a56e6048a39473391956f8b96449f6c73675fdf7507d6638af9b5e65afbbbdce8733a0be3fdc9')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
