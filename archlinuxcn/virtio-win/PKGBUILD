# Maintainer: Javier Tiá <javier dot tia at gmail dot com>

pkgname=virtio-win
_ver=0.1.164
# package version
pkgver=${_ver}.2
# upstream version
_pkgver=${_ver}-2
pkgrel=1
pkgdesc='virtio drivers for Windows (2000, XP, Vista, 7, 8, 10) guests and floppy images for Windows XP'
arch=('any')
url='https://docs.fedoraproject.org/en-US/quick-docs/creating-windows-virtual-machines-using-virtio-drivers/index.html'
license=('GPL2')
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
sha256sums=('594678f509ba6827c7b75d076ecfb64d45c6ad95e9fccba7258e6eee9a6a3560'
            'd83eda5ccfd65ed5be444050363f6e3a54a7468c977a64605e5bec7272a4e716'
            '823757c380711f91841153b67067185197d336b5a83a70530f005c81cdafbb21')

package() {
  install -Dm 644 ${pkgname}-${_pkgver}.iso \
    "${pkgdir}/usr/share/virtio/${pkgname}.iso"

  install -Dm 644 ${pkgname}-${_pkgver}_amd64.vfd \
    "${pkgdir}/usr/share/virtio/${pkgname}_x86_64.vfd"

  install -Dm 644 ${pkgname}-${_pkgver}_x86.vfd \
    "${pkgdir}/usr/share/virtio/${pkgname}_x86_32.vfd"
}

# vim:set ts=2 sw=2 et:
