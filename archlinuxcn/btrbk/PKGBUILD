# Maintainer: Michael Duell < mail at akurei dot me >
# Contributor: Myles English <myles at rockhead dot biz>
pkgname=btrbk
pkgver=0.32.4
pkgrel=1
pkgdesc="Backup tool for btrfs subvolumes, taking advantage of btrfs specific capabilities to create atomic snapshots and transfer them incrementally to your backup locations"
url="https://digint.ch/btrbk"
arch=('any')
license=('GPL3')
depends=('perl' 'btrfs-progs')
makedepends=('asciidoctor')
optdepends=('openssh: remote backup support',
        'mbuffer: --progress support and add buffering to send-stream'
        'sudo: support for the btrfs-progs-sudo backend')
source=("https://digint.ch/download/btrbk/releases/${pkgname}-${pkgver}.tar.xz")

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" BINDIR="/usr/bin" install
}

b2sums=('e76a0b6ed8d54f97fa0ac2dad139891ae0f9450095e08d560f5a62ad28e3cc2e39da0a3a094ca841c5debbe9d34ca1cb3930cb3a16877b1547fb81f9c5e7e244')
