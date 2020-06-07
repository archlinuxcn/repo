# Maintainer: oldherl <oldherl@gmail.com>

pkgname=skychart-data-stars
pkgname=(skychart-data-stars)
pkgver=4.0
pkgrel=1
pkgdesc="Standard stars catalog for skychart, down to magnitude 12, variables and double stars: Tycho2, GCVS, WDS. Search index for SAO, BD, HD, GC"
arch=(any)
license=('GPL')
url="http://www.ap-i.net/skychart/start"
source=(
"https://downloads.sourceforge.net/project/skychart/2-catalogs/Stars/skychart-data-stars-4.0-3421-linux_all.tar.bz2"
)
sha1sums=("e2046c5be315a0964d4d969e44719372987747db")

package_skychart-data-stars() {
  depends=('skychart>=4.0')
  mkdir -p "${pkgdir}"/usr/share/skychart/
  cp -a "$srcdir/share/skychart/cat"  "${pkgdir}/usr/share/skychart/cat"
}
