# Maintainer: Javier Tiá <javier dot tia at gmail dot com>

pkgname=virtio-win
_ver=0.1.173
# upstream version
_pkgver=${_ver}-8
# package version
pkgver=${_ver}.8
pkgrel=1
pkgdesc='virtio drivers for Windows (2000, XP, Vista, 7, 8, 10) guests and floppy images for Windows XP'
arch=('any')
url='https://docs.fedoraproject.org/en-US/quick-docs/creating-windows-virtual-machines-using-virtio-drivers/index.html'
license=('BSD-3-Clause')
optdepends=('qemu')
# https://fedorapeople.org/groups/virt/virtio-win/CHANGELOG
changelog="${pkgname}.changelog"
# install="${pkgname}.install"
_url=https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio
source=("${pkgname}-${_pkgver}.iso::${_url}/${pkgname}-${_pkgver}/${pkgname}.iso"
        "${pkgname}-${_pkgver}_amd64.vfd::${_url}/${pkgname}-${_pkgver}/${pkgname}_amd64.vfd"
        "${pkgname}-${_pkgver}_x86.vfd::${_url}/${pkgname}-${_pkgver}/${pkgname}_x86.vfd")
noextract=("${pkgname}-${_pkgver}.iso"
           "${pkgname}-${_pkgver}_amd64.vfd"
           "${pkgname}-${_pkgver}_x86.vfd")
sha256sums=('f6726d8f6a7c6e50835eb46878ec7eae4dd540fec557cd1760052e07c0368c04'
            '4a2a50bc06aa6c1b0baec580a1c74ea3552f7da6388b74455cd19423f0a01cf3'
            '05ab65be9b592ac2824a3b094b8d25b5eec11f16e263010a5fcf31c7251ec6ec')

package() {
  install -Dm 644 ${pkgname}-${_pkgver}.iso \
    "${pkgdir}/usr/share/virtio/${pkgname}.iso"

  install -Dm 644 ${pkgname}-${_pkgver}_amd64.vfd \
    "${pkgdir}/usr/share/virtio/${pkgname}_x86_64.vfd"

  install -Dm 644 ${pkgname}-${_pkgver}_x86.vfd \
    "${pkgdir}/usr/share/virtio/${pkgname}_x86_32.vfd"
}

# vim:set ts=2 sw=2 et:
