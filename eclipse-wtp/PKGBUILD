# Maintainer: Arthur Zamarin <arthurzam@gmail.com>
# Contributor: Shanto <shanto@hotmail.com>
# Contributor: Jonathan Wiersma <archaur at jonw dot org>

pkgname=eclipse-wtp
pkgver=3.8.0
_pkgdate=20160608130753
pkgrel=1
pkgdesc="Webtools framework for the Eclipse platform"
url="http://www.eclipse.org/webtools/"
license=("Eclipse Public License")
arch=('any')
depends=( 'eclipse' 'eclipse-emf' 'eclipse-gef' 'java-runtime>=5' )
optdepends=("java-environment>=5" "eclipse-dtp")
provides=('eclipse-wtp-wst')
options=(!strip)
_mirror="http://www.eclipse.org/downloads/download.php?r=1&mirror_id=1&file="
source=("$_mirror/webtools/downloads/drops/R$pkgver/R-$pkgver-$_pkgdate/wtp-repo-R-$pkgver-$_pkgdate.zip")
sha256sums=('86f558189ced7dba01e40074ae862a710c6dd3bd81c81ad0d0bdcacab2e0a507')

package() {
  _dest="$pkgdir/usr/lib/eclipse/dropins/wtp/"
  
  cd "$srcdir"
  mkdir -p "${_dest}"
  
  cp -r {features,plugins} "$_dest/"

  find "$pkgdir/usr/lib/eclipse" -type d -exec chmod 755 {} \;
  find "$pkgdir/usr/lib/eclipse" -type f -exec chmod 644 {} \;
}
