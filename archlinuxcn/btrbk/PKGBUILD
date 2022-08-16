# Maintainer: Michael Duell < mail at akurei dot me >
# Contributor: Myles English <myles at rockhead dot biz>
pkgname=btrbk
pkgver=0.32.3
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

b2sums=('f0e389891bfdfa961187505548ec5139aa8967932d2fcca43c151c8ca25664c30af96f0f52531507e7c838ca3df16f371f7419df226283734fee23f6af56b3cf')
