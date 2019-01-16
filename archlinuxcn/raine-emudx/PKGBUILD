# Maintainer: carstene1ns <arch carsten-teibes de> - http://git.io/ctPKG
# Contributor: robb_force <robb_force@holybuffalo.net>

pkgname=raine-emudx
pkgver=20080514
pkgrel=2
pkgdesc="Improved graphic and sound files for some games in the Raine emulator"
arch=('any')
url="http://raine.1emulation.com/download/extras.html"
license=('unknown')
depends=('raine')
source=("http://raine.1emulation.com/archive/emudx/dkongg.dx2"
        "http://raine.1emulation.com/archive/emudx/froggerg.dx2"
        "http://raine.1emulation.com/archive/emudx/galdxg.dx2"
        "http://raine.1emulation.com/archive/emudx/mspacmang.dx2"
        "http://raine.1emulation.com/archive/emudx/pacmang.dx2"
        "http://raine.1emulation.com/archive/emudx/dkongm.dx2"
        "http://raine.1emulation.com/archive/emudx/froggerm.dx2"
        "http://raine.1emulation.com/archive/emudx/galdxm.dx2"
        "http://raine.1emulation.com/archive/emudx/mspacmanm.dx2"
        "http://raine.1emulation.com/archive/emudx/pacmanm.dx2")
sha256sums=('9d59d7e5742c7c7d8d140488acf9e1f6c718ff8552f6a9bafcd5fd828e33edfc'
            'ede281a1c328d577b81fdf29b66f5c055f58e8a0a347e69ab2519ecca34ce167'
            'f867a7c7a3dde51d5ae870f1c55e63d4c23f43b5351cf4c8aa4ad60ea8091ab5'
            '7bc376633fe6513377d5be5ffbf48030d6c6a89179cc4d98d6d503b959838022'
            '3227b6879735bed75d4ef59227ce226845b45e9bce56935a40209cc4c4d1162d'
            'fb83a42f93abad225e8dd6a160b4e268ef1cbc1488fca8ad520f43295173796c'
            'f70e863b79b719fb444126e15575b909cafb9249e21b4c0615a43d2c490abff4'
            'c5b09f0a625710a31ddc3d8f0aa796ed22e53a94fd0c60143fd738ee2486ca63'
            '23d397bd4e590f4d77c147ee28431983d10e707a1027ed61028363d9640dec74'
            'e9422c4f05231fdb3600ec2a789d5016c8bc6386cab38ced5dae9382734a4ff9')

package() {
  install -d "$pkgdir"/usr/share/raine/emudx
  install -m644 *.dx2 "$pkgdir"/usr/share/raine/emudx
}
