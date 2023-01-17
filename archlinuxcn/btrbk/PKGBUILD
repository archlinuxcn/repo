# Maintainer: Michael Duell < mail at akurei dot me >
# Contributor: Myles English <myles at rockhead dot biz>
pkgname=btrbk
pkgver=0.32.5
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

b2sums=('036a2b5c31a308dbc1efc7a27211f89dfc07bcfcead49deb68a2e8313aec9539483ef3a91481f4ebaa9d2b4817b202ced1945a30ed7fc9b51f1336878b2f17d7')
