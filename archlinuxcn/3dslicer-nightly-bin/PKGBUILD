# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=3dslicer-nightly-bin
_pkgname=3dslicer
pkgver=4.13.0.r20201209
pkgrel=1
pkgdesc="A multi-platform, free open source software package for visualization and medical image computing (nightly build)"
arch=('x86_64')
url="https://www.slicer.org"
license=('BSD')
depends=(
  'dbus'
  'glib2'
)
makedepends=('gendesk')
provides=(3dslicer=${pkgver})
conflicts=('3dslicer')
source=(
    "${_pkgname}-${pkgver}.tar.gz::http://download.slicer.org/download?os=linux&stability=nightly"
    "${_pkgname}.svg::https://github.com/Slicer/Slicer/raw/master/Resources/3DSlicerLogo-app-icon.svg"
)
noextract=("${_pkgname}.tar.gz")
sha512sums=('4ca84c5b87035f902fe5e1a9b19992683ab11ed3061eea8bc114394873e728c6c804f5e28d03ba1bb1e96ae728f09fea4c11087e3bcd03fb86621b44982189c7'
            'c23104efcbec3d49b5c26ad5514ed74316423db4aa9e6c7894f02f7ddbe509b577de358dfdd2f7c492963f312b7c146f03d5e41a89ab1298811894dc18746225')
options=('!strip' '!emptydirs')

prepare() {
# manually extract tarball due to their unpredicted name
  mkdir "${srcdir}/${_pkgname}"
  tar xvf "${srcdir}/${_pkgname}-${pkgver}.tar.gz" -C "${srcdir}/${_pkgname}" --strip-components 1

  echo "Creating desktop file"
  gendesk -f -n --pkgname ${_pkgname} \
    --pkgdesc "${pkgdesc}" \
    --categories "Graphics;MedicalSoftware;Science;" \
    --icon "${_pkgname}" \
    --exec "Slicer"
}

package() {
  install -d "${pkgdir}/opt" "${pkgdir}/usr/bin"
  mv -v "${srcdir}/${_pkgname}" "${pkgdir}/opt"
  ln -s /opt/${_pkgname}/Slicer "${pkgdir}/usr/bin"
  install -Dm644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
  install -Dm644 "${srcdir}/${_pkgname}.svg" "${pkgdir}/usr/share/pixmaps/${_pkgname}.svg"
}
# vim:set ts=2 sw=2 et:

