# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=streamlit-webrtc
pkgname=python-streamlit-webrtc
pkgver=0.41.0
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
sha512sums=('ddd62c45ab5f0be7aa647af1684019c8a1d1cc62e7cdc49f3072b05ad52addc51eaf047b70a430c0cecfa84ab98596c72a8184df42fc0b4ee732fd3185cfd220')

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
