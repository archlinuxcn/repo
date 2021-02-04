# Maintainer: Michael Duell < mail at akurei dot me >
# Contributor: Myles English <myles at rockhead dot biz>
pkgname=btrbk
pkgver=0.31.0
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

sha384sums=('64fe025d10ac5c39ef2a7ebaaf02ae077ffee286444160590cb2890d249c399aa16a454630ed307ff5420eefe6c1b525')
