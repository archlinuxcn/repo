# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=streamlit-webrtc
pkgname=python-streamlit-webrtc
pkgver=0.43.3
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
sha512sums=('a62f21091c7629fd4da5474f00cf8d4b7e10a91900ad9895b36901bdce1bcf544ef470e2498c86e520336a056d480475073407abd1914d5acc2d8d69bcde5c2d')

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
