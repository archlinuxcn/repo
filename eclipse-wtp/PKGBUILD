# Maintainer: Arthur Zamarin <arthurzam@gmail.com>
# Contributor: Shanto <shanto@hotmail.com>
# Contributor: Jonathan Wiersma <archaur at jonw dot org>

pkgname=eclipse-wtp
pkgver=3.6.3
_pkgdate=20150216091848
pkgrel=1
pkgdesc="Webtools framework for the Eclipse platform"
url="http://www.eclipse.org/webtools/"
license="Eclipse Public License"
arch=('any')
depends=( 'eclipse' 'eclipse-emf' 'eclipse-gef' 'java-runtime>=5' )
optdepends=("java-environment>=5" "eclipse-dtp")
provides=('eclipse-wtp-wst')
options=(!strip)
_mirror="http://www.eclipse.org/downloads/download.php?r=1&mirror_id=1&file="
source=("$_mirror/webtools/downloads/drops/R$pkgver/R-$pkgver-$_pkgdate/wtp4x-repo-R-$pkgver-$_pkgdate.zip")
sha256sums=('3dd7f464c7abee2e3d4e76a3ebfd9590145169ce9eb26ca739659875019204cf')

package() {
  _dest="$pkgdir/usr/share/eclipse/dropins/wtp/"
  
  cd "$srcdir"
  mkdir -p "${_dest}"
  
  cp -r {features,plugins} "$_dest/"

  find "$pkgdir/usr/share/eclipse" -type d -exec chmod 755 {} \;
  find "$pkgdir/usr/share/eclipse" -type f -exec chmod 644 {} \;
}
