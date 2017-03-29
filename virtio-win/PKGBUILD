# Maintainer: Javier Tiá <javier dot tia at gmail dot com>

pkgname=virtio-win
_ver=0.1.134
# package version
pkgver=${_ver}.3
# upstream version
_pkgver=${_ver}-3
pkgrel=1
pkgdesc="virtio drivers for Windows (2000, XP, Vista, 7, 8, 10) guests and floppy images for Windows XP"
arch=('any')
url="https://fedoraproject.org/wiki/Windows_Virtio_Drivers"
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
sha256sums=('3556f6570d6b3a916974a476f59871f965bed86e2a8976beb9493490af79edc4'
            '601862f842a5b7a0f9cb98d26d060409c956f414812682b4900885eb8e44668c'
            'aa81f36a8d9c1c502ad63e140691f5f55d6c3774925ea8ff34268cd6974b8fb4')

package() {
  install -Dm 644 ${pkgname}-${_pkgver}.iso \
    "${pkgdir}/usr/share/virtio/${pkgname}.iso"

  install -Dm 644 ${pkgname}-${_pkgver}_amd64.vfd \
    "${pkgdir}/usr/share/virtio/${pkgname}_x86_64.vfd"

  install -Dm 644 ${pkgname}-${_pkgver}_x86.vfd \
    "${pkgdir}/usr/share/virtio/${pkgname}_x86_32.vfd"
}

# vim:set ts=2 sw=2 ft=sh et:
