# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=3dslicer-bin
_pkgname=3dslicer
pkgver=4.10.2
pkgrel=1
pkgdesc="A multi-platform, free open source software package for visualization and medical image computing"
arch=('x86_64')
url="https://www.slicer.org"
license=('BSD')
depends=('dbus' 'glib2')
makedepends=('gendesk')
provides=('3dslicer')
conflicts=('3dslicer')
source=(
    "${pkgname}-${pkgver}.tar.gz::https://download.slicer.org/bitstream/1023242"
    "${_pkgname}.svg::https://www.slicer.org/w/images/9/9f/3DSlicerLogo-HorizontalF.svg"
)
sha512sums=('36f1b175f987e7d1e288f08d55c6942e494f1234bfdfb4ffae8517bb1711418c6ae3d5efd3f57dc31a7f65c451c8324d8c09d4de697b6b81d0a85ec48299c686'
            '67986a7bd90c95c4a91ddaecd86ceb3b54729f62c7e19ba3559f6180659902275a2f5a794cada3e9412664fb97cc6d57a02055826c4c135f2005d2c92d0ef878')

prepare() {
  msg2 "Creating desktop file"
  gendesk -f -n --pkgname ${_pkgname} \
    --pkgdesc "${pkgdesc}" \
    --categories "Graphics;MedicalSoftware;Science;" \
    --icon "${_pkgname}" \
    --exec "Slicer"
}
package() {
  install -d "${pkgdir}/opt" "${pkgdir}/usr/bin"
  mv "${srcdir}/Slicer-${pkgver}-linux-amd64" "${pkgdir}/opt/${_pkgname}"
  ln -s /opt/${_pkgname}/Slicer "${pkgdir}/usr/bin"
  install -Dm644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
  install -Dm644 "${srcdir}/${_pkgname}.svg" "${pkgdir}/usr/share/pixmaps/${_pkgname}.svg"
}
# vim:set ts=2 sw=2 et:

