# Maintainer: oldherl <oldhderl@gmail.com>

pkgbase=skychart-data-dso
pkgname=(skychart-data-dso)
pkgver=4.0
pkgrel=1
pkgdesc="All the standard nebulae catalog for skychart: NGC, PGC, GCM, GPN, LBN, OCL, including 5 million galaxies from Hyperleda 2017"
arch=(any)
license=('GPL')
url="http://www.ap-i.net/skychart/start"
source=(
"https://downloads.sourceforge.net/project/skychart/2-catalogs/Nebulea/skychart-data-dso-4.0-3431-linux_all.tar.bz2"
)
sha1sums=('d62ee54467eb44f94593f982a786afe9ee6ba3fa')

package_skychart-data-dso() {
  depends=('skychart>=4.0')
  mkdir -p "${pkgdir}"/usr/share/skychart/
  cp -a "$srcdir/share/skychart/cat"  "${pkgdir}/usr/share/skychart/cat"
}
