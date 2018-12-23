# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>
# Contributor: Simon Lipp <sloonz+aur at gmail dot com>

pkgname=jrosetta
pkgver=1.0.4
pkgrel=4
pkgdesc="Graphical console engine for Swing"
arch=('any')
url="http://dev.artenum.com/projects/JRosetta/"
license=('GPL2')
depends=('java-runtime')
makedepends=()
# original upstream
#source=(
#"http://maven.artenum.com/content/groups/public/com/artenum/jrosetta/jrosetta-api/$pkgver/jrosetta-api-$pkgver.jar"
#"http://maven.artenum.com/content/groups/public/com/artenum/jrosetta/jrosetta-engine/$pkgver/jrosetta-engine-$pkgver.jar"
#)
#
# backup
source=(
"jrosetta-api-1.0.4.jar::https://www.dropbox.com/s/f35kiamng3nj18q/jrosetta-api-1.0.4.jar?dl=1"
"jrosetta-engine-1.0.4.jar::https://www.dropbox.com/s/tfx4m3u4fcxoj8l/jrosetta-engine-1.0.4.jar?dl=1"
)
# mirror (died)
#source=("http://aur.pallissard.net/MRWITEK/jrosetta-api-1.0.4.jar"
#"http://aur.pallissard.net/MRWITEK/jrosetta-engine-1.0.4.jar")
md5sums=('00082a2e745c8e0042608650334a9aaf' 'cdef53b29bce0ccd46d9986996df40a6')
noextract=("jrosetta-engine-$pkgver.jar" "jrosetta-api-$pkgver.jar")

package() {
      cd "$srcdir"
      install -Dm644 "$srcdir/$pkgname-api-$pkgver.jar" "$pkgdir/usr/share/java/$pkgname/$pkgname-API.jar"
      install -Dm644 "$srcdir/$pkgname-engine-$pkgver.jar" "$pkgdir/usr/share/java/$pkgname/$pkgname-engine.jar"
}
