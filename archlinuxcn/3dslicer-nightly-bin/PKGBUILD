# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=3dslicer-nightly-bin
_pkgname=3dslicer
pkgver=4.11.0.r5266433
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
    "${_pkgname}.tar.gz::http://download.slicer.org/download?os=linux&stability=nightly"
    "${_pkgname}.svg::https://github.com/Slicer/Slicer/raw/master/Resources/3DSlicerLogo-app-icon.svg"
)
noextract=("${_pkgname}.tar.gz")
sha512sums=('eeaccb0d243cf92eb6037fc00a7768ea9faabb42c33d0e729285f352307e7fac2a36fb4f15f35d66b9143ea7ff07b8097618b7b3fa4f39143d0e7a59a6d1e7fe'
            'c23104efcbec3d49b5c26ad5514ed74316423db4aa9e6c7894f02f7ddbe509b577de358dfdd2f7c492963f312b7c146f03d5e41a89ab1298811894dc18746225')

prepare() {
# manually extract tarball due to their unpredicted name
  mkdir "${srcdir}/${_pkgname}"
  tar xvf "${srcdir}/${_pkgname}.tar.gz" -C "${srcdir}/${_pkgname}" --strip-components 1

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

