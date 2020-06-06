# Maintainer: oldherl <oldhderl@gmail.com>

pkgname=skychart-data-pictures
pkgver=4.0
pkgrel=1
pkgdesc="DSO pictures for skychart. 9700 pictures for object of the SAC and OpenNGC catalog."
arch=(any)
license=('GPL')
depends=('skychart>=4.0')
url="http://www.ap-i.net/skychart/start"
source=(
"https://sourceforge.net/projects/skychart/files/2-catalogs/Nebulea/skychart-data-pictures-4.0-3421-linux_all.tar.bz2"
)
sha1sums=("5ae47783d592fb1feeb53097727a8dde3808d97b")
# This package contains only pictures. To save time, don't strip
options=(!strip)

package() {
  mkdir -p "${pkgdir}"/usr/share/skychart/
  cp -a "$srcdir/share/skychart/data"  "${pkgdir}/usr/share/skychart/data"
}
