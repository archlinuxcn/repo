# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

pkgname=macports-base
pkgver=2.5.4
pkgrel=1
epoch=1
pkgdesc='The MacPorts command-line client'
url='https://www.macports.org/'
arch=('i686' 'x86_64')
license=('BSD')
depends=('curl' 'openssl' 'sqlite')
# tcl: MacPorts comes with its own vendored tclsh, while a system interpreter
# is still needed to build tcllib
makedepends=('tcl' 'nmtree')
optdepends=(
  'rsync: for syncing sources via rsync'
  'nmtree: for building ports'
)
source=("https://github.com/macports/macports-base/releases/download/v$pkgver/MacPorts-$pkgver.tar.bz2"{,.asc})
sha256sums=('0276c6cf9a9adbb65743ffcfbb3b0c3425ae22431d58c77e353d35c89e898e8b'
            'SKIP')
validpgpkeys=(
  'C403793657236DCF2E580C0201FF673FB4AAE6CD'  # Joshua Root <jmr@macports.org>
)
backup=(opt/local/etc/macports/archive_sites.conf
        opt/local/etc/macports/macports.conf
        opt/local/etc/macports/pubkeys.conf
        opt/local/etc/macports/sources.conf
        opt/local/etc/macports/variants.conf)

build() {
  cd MacPorts-$pkgver

  # provide paths manually so that these packages are not necessray during building
  MAN=/usr/bin/man \
  MTREE=/usr/bin/mtree \
  RSYNC=/usr/bin/rsync \
  ./configure \
    --enable-readline

  make
}

package() {
  cd MacPorts-$pkgver
  make DESTDIR="$pkgdir" install

  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
