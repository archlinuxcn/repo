# Maintainer: Kyle McNally <kyle@kmcnally.net>
# Contributor: John Williams <jwilliams4200 liamg reverse&remove moc>
pkgname=snapraid
pkgver=14.4
pkgrel=1
pkgdesc="tool for Snapshot RAID: generate parity files, maintain checksums on data, restore lost data"
arch=('x86_64' 'i686')
url="http://www.snapraid.it/"
license=('GPL3')
depends=('libutil-linux' 'glibc')
optdepends=(
  'smartmontools: needed for snapraid smart'
  'snapraid-daemon: daemon for SnapRAID ux/ui'
)
source=("https://github.com/amadvance/${pkgname}/releases/download/v${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('941467eb69a055028a68484c83aef6b193808914729ab3d3efe0cfd47c2352ab')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  ./configure --prefix="/usr"
  make
}

check() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  echo "========================================================================="
  echo "=================== NOTICE: Regression test started ====================="
  echo "=== Please ignore any error message printed below, they are expected! ==="
  echo "========================================================================="
  sleep 5s # Waits 5 seconds.
  make check
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}/" prefix="/usr" mandir="/usr/share/man" install

  # documentation
  install -D -m644 snapraid.conf.example ${pkgdir}/usr/share/${pkgname}/snapraid.conf.example
  install -D -m644 AUTHORS ${pkgdir}/usr/share/doc/${pkgname}/AUTHORS
  install -D -m644 COPYING ${pkgdir}/usr/share/doc/${pkgname}/COPYING
  install -D -m644 HISTORY ${pkgdir}/usr/share/doc/${pkgname}/HISTORY
  install -D -m644 INSTALL ${pkgdir}/usr/share/doc/${pkgname}/INSTALL
  install -D -m644 README ${pkgdir}/usr/share/doc/${pkgname}/README
  install -D -m644 CHECK ${pkgdir}/usr/share/doc/${pkgname}/CHECK
  install -D -m644 TODO ${pkgdir}/usr/share/doc/${pkgname}/TODO
}
