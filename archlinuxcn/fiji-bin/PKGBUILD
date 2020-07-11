# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=fiji
pkgname=fiji-bin
pkgver=20200711.0516
pkgrel=1
epoch=2
pkgdesc="ImageJ distribution with a lot of plugins for scientific (especially biology related) image processing."
arch=('x86_64')
url='http://fiji.sc/'
license=('GPL')
depends=(
  'freetype2'
  'libnet'
)
makedepends=('gendesk')

source=("${pkgname}-${pkgver}.zip::https://downloads.imagej.net/fiji/archive/${pkgver/./-}/fiji-linux64.zip")
sha256sums=('0f35bf8f2bdac058a4ede840567aba640b503dba4d37f127d181091074ca5041')


prepare() {
  echo "Creating desktop file"
  gendesk -f -n --pkgname ${_pkgname} \
    --pkgdesc "${pkgdesc}" \
    --categories "Graphics;Science;ImageProcessing;" \
    --icon "${_pkgname}" \
    --exec ${_pkgname}
}

package()
{
  install -d "${pkgdir}/opt" "${pkgdir}/usr/bin" "${pkgdir}/usr/share/pixmaps"
  mv "${srcdir}/Fiji.app" "${pkgdir}/opt/${_pkgname}"
  cp "${pkgdir}/opt/${_pkgname}/images/icon.png" "${pkgdir}/usr/share/pixmaps/${_pkgname}.png"
  ln -s "/opt/${_pkgname}/ImageJ-linux64" "${pkgdir}/usr/bin/${_pkgname}"
  install -Dm644 "${srcdir}/fiji.desktop" "${pkgdir}/usr/share/applications/fiji.desktop"
}
