# Maintainer: Javier Tiá <javier dot tia at gmail dot com>

pkgname=virtio-win
_ver=0.1.118
pkgver=${_ver}.2
pkgver_=${_ver}-2
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
source=("${_url}/${pkgname}-${pkgver_}/${pkgname}.iso"
        "${_url}/${pkgname}-${pkgver_}/${pkgname}_amd64.vfd"
        "${_url}/${pkgname}-${pkgver_}/${pkgname}_x86.vfd")
noextract=("${pkgname}.iso" "${pkgname}_amd64.vfd" "${pkgname}_x86.vfd")
sha256sums=('1fcc4013272e7bdc36d074c9ee30f1eba291c7f822b7d04a2db9d1862d2f31bd'
            'cbdaea2f00cd3b6eda32209ae6c9c2bb938dcc52ceb464ebf9ce9c0bd6f3fbf8'
            'd505ebf5b7d2d5822a275faf4417d87f013909944d5293dcf4bc634e214adb67')

package() {
  install -Dm 644 ${pkgname}.iso \
    "$pkgdir/usr/share/virtio/${pkgname}.iso"
  install -Dm 644 ${pkgname}_amd64.vfd \
    "$pkgdir/usr/share/virtio/${pkgname}_x86_64.vfd"
  install -Dm 644 ${pkgname}_x86.vfd \
    "$pkgdir/usr/share/virtio/${pkgname}_x86_32.vfd"
}

# vim:set ts=2 sw=2 ft=sh et:
