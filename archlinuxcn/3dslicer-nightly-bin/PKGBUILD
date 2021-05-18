# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=3dslicer-nightly-bin
_pkgname=3dslicer
pkgver=4.13.0.r20210518
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
    "${_pkgname}.svg::https://github.com/Slicer/Slicer/raw/v4.11/Resources/3DSlicerLogo-app-icon.svg"
)
noextract=("${_pkgname}.tar.gz")
sha512sums=('84408354fb50a424303432867f731772cea4eee477fefa4b0b1bd0c7d6178d083d07b9892a8e402cc6cf8e63c8eee986d1100ce9ac4cd44245bc54d58299dfcc'
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

