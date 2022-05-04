# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=streamlit-webrtc
pkgname=python-streamlit-webrtc
pkgver=0.37.0
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
sha512sums=('88101b3f19dd2e5ab5556cb7a41f30566f81db508ba4d077ce57babe515cce5af017133a6d950c525ba8adbd667f5c4cf26d6285a6c0d77289f0bb7509b43b02')

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
