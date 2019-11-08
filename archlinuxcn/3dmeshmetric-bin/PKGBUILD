# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=3dmeshmetric-bin
_pkgname=3DMetricTools
pkgver=1.4.3
pkgrel=1
pkgdesc="A visualization tool based on the VTK library."
arch=('x86_64')
url="https://www.nitrc.org/projects/meshmetric3d/"
license=('GPL')
depends=(
  'gcc-libs'
  'zlib'
)
makedepends=('gendesk')
provides=(3dmeshmetric=${pkgver})
conflicts=(3dmeshmetric)
source=(
    "${pkgname}-${pkgver}.tar::https://www.nitrc.org/frs/download.php/6714/3DMetricTools${pkgver}-Linux.tar"
)
sha512sums=('c62a252b6583fc4ee7d5e92f8538b152aa98baf1ca217d72d0f3ffeb61234e54ef37bed8d1a212c752bbb97c5eff4c28a655a3dfcc0c399b5600352746a4eea3')

prepare() {
  msg2 "Creating desktop file"
  gendesk -f -n --pkgname ${_pkgname} \
    --pkgdesc "${pkgdesc}" \
    --categories "Graphics;MedicalSoftware;Science;" \
    --icon "${_pkgname}" \
    --exec "meshMetric"
}

package() {
  install -d "${pkgdir}/opt" "${pkgdir}/usr/bin" "${pkgdir}/usr/share/pixmaps"
  mv "${srcdir}/${_pkgname}${pkgver}-Linux" "${pkgdir}/opt/${_pkgname}"
  cp "${pkgdir}/opt/${_pkgname}/icons/MeshMetric.png" "${pkgdir}/usr/share/pixmaps/${_pkgname}.png"
  ln -s /opt/${_pkgname}/meshMetric "${pkgdir}/usr/bin/meshMetric"
  ln -s /opt/${_pkgname}/ModelToModelDistance "${pkgdir}/usr/bin/ModelToModelDistance"
  install -Dm644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
}
# vim:set ts=2 sw=2 et:

