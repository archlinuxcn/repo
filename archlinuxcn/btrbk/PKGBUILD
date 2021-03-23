# Maintainer: Michael Duell < mail at akurei dot me >
# Contributor: Myles English <myles at rockhead dot biz>
pkgname=btrbk
pkgver=0.31.2
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

b2sums=('a05ef8a665d50b0f9637b1bc7026f0ca0f8364377b4165dae09cd27790dc139aaea1096a54719d948adda5050f91580650bf58db70a086cfdd14b73559fad9f3')
