# Maintainer: juantascon <juantascon.aur@horlux.org>

pkgname=plantuml
pkgver=8030
pkgrel=1
pkgdesc="Component that allows to quickly write uml diagrams"
arch=(any)
url="http://plantuml.sourceforge.net/"
license=('GPL')
depends=("java-runtime" "graphviz")
makedepends=("apache-ant" "java-environment")
source=(http://downloads.sourceforge.net/project/$pkgname/$pkgname-$pkgver.tar.gz "$pkgname.run")
sha256sums=('325a2f2fe9d9a05f9f2e10842612863b0cf821e2a2280b6f4e495d34e2606f92'
            'dff39e4d8dd8eedb58c1b0a0cf64ab2c404b713e3a42fa5fdf0b6792ca382ed5')

package() {
  install -m 755 -D "$pkgname.run" "$pkgdir/usr/bin/$pkgname"
  
  cd "$srcdir/$pkgname-$pkgver"
  ant dist
  install -m 644 -D "$pkgname.jar" "$pkgdir/opt/$pkgname/$pkgname.jar"
}
