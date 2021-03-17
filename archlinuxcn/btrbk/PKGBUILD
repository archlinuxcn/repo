# Maintainer: Michael Duell < mail at akurei dot me >
# Contributor: Myles English <myles at rockhead dot biz>
pkgname=btrbk
pkgver=0.31.1
pkgrel=1
pkgdesc="Backup tool for btrfs subvolumes, taking advantage of btrfs specific capabilities to create atomic snapshots and transfer them incrementally to your backup locations"
url="https://digint.ch/btrbk"
arch=('any')
license=('GPL3')
depends=('perl' 'btrfs-progs')
conflicts=('btrbk-git')
makedepends=('asciidoctor')
options=('!makeflags') # temporary fix for https://github.com/digint/btrbk/pull/341
optdepends=('openssh: remote backup support',
        'mbuffer: --progress support and add buffering to send-stream')
source=("https://digint.ch/download/btrbk/releases/${pkgname}-${pkgver}.tar.xz")

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" BINDIR="/usr/bin" install
}

b2sums=('0e9b1acf5f784c28c3c80c9b391d69b619c0b2054ec9c73ed8425c8a0fe4211d1559bd399bb63f61937d4ba8cf94f10656a2863383688d00f737de403dedcebd')
