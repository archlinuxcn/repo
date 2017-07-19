# Maintainer: Javier Tiá <javier dot tia at gmail dot com>

pkgname=virtio-win
_ver=0.1.140
# package version
pkgver=${_ver}.1
# upstream version
_pkgver=${_ver}-1
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
sha256sums=('7f74845071f738e151ba71e7e3bba4f5bd980de8111aa5de127d488143ac88f8'
            '8de08f02bfe36a029621976cad1d714453cce8ef6c3dabb68efab1eb75c3b163'
            '2090cd6a1cc8af3e56bd29a2ab16dd86fc0789aa5661b089f54564a40ed79ad1')

package() {
  install -Dm 644 ${pkgname}-${_pkgver}.iso \
    "${pkgdir}/usr/share/virtio/${pkgname}.iso"

  install -Dm 644 ${pkgname}-${_pkgver}_amd64.vfd \
    "${pkgdir}/usr/share/virtio/${pkgname}_x86_64.vfd"

  install -Dm 644 ${pkgname}-${_pkgver}_x86.vfd \
    "${pkgdir}/usr/share/virtio/${pkgname}_x86_32.vfd"
}

# vim:set ts=2 sw=2 ft=sh et:
