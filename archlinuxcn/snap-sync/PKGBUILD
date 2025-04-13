# Maintainer: NicoHood <archlinux {cat} nicohood {dog} de>
# PGP ID: 97312D5EB9D7AE7D0BD4307351DAE9B7C1AE9161
# Contributor: Wes Barnett <wes at wbarnett dot us>
pkgname=snap-sync
pkgver=0.7
pkgrel=3
pkgdesc="Use snapper snapshots to backup to external drive"
arch=(any)
url="https://github.com/wesbarnett/snap-sync"
license=('GPL2')
depends=(snapper btrfs-progs which)
optdepends=('pv: progress bar during backup'
            'libnotify: desktop notifications'
            'rsync: sending info.xml to remote hosts'
            'openssh: sending snapshots to remote destination'
            'sudo: use sudo for remote snapshots')
install='snap-sync.install'
source=("${pkgname}-${pkgver}.tar.gz::${url}/releases/download/${pkgver}/${pkgname}-${pkgver}.tar.gz"
        "${pkgname}-${pkgver}.tar.gz.sig::${url}/releases/download/${pkgver}/${pkgname}-${pkgver}.tar.gz.sig"
        'snap-sync.install')
validpgpkeys=('8535CEF3F3C38EE69555BF67E4B5E45AA3B8C5C3'  # old key
              'F7B28C61944FE30DABEEB0B01070BCC98C18BD66') # new ecc key
sha512sums=('de38038e856f1b9d889e6f8a8a29380265650fc582ee23914e16bc3de639e9e25438d7ec876afd58d35feb0f7a7ee4f62625bfa02eca29a7b18566fce58deb08'
            'SKIP'
            '39b4e05794657b880a81d8060f34a6a703db8169b68963aa1cc32e428a7a593b2d65dc6eb1f3fe37b7a0f2967c02113d1368b5d090341ed3856871d141013590')

package() {
    cd "${pkgname}"
    make SNAPPER_CONFIG=/etc/conf.d/snapper DESTDIR="${pkgdir}" install
}
