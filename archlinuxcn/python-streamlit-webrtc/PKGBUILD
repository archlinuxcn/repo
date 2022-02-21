# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=streamlit-webrtc
pkgname=python-streamlit-webrtc
pkgver=0.35.0
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
sha512sums=('42718a0e1c1980f9efd12fa43c137ce3ad8cea2aa89f56fd059c76e6d3a9b8f1dfb9e93d506be7ee3d4e82ecc9667893eac5fe50ddeff49542538ffa43ebd338')

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
