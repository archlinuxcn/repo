# Maintainer: Gordin <9ordin @t gmail.com>
# Contributor: Hunter Haugen <h.haugen@gmail.com>
pkgname=pidgin-blinklight
pkgver=0.11.1
pkgrel=3
pkgdesc="This plugin for Pidgin will blink your ThinkPad's ThinkLight or Asus light when you get new messages"
arch=('i686' 'x86_64')
url="http://debian.mirror.inra.fr/debian/pool/main/p/pidgin-blinklight/"
license=('GPL')
depends=('pidgin')
source=(http://debian.mirror.inra.fr/debian/pool/main/p/pidgin-blinklight/${pkgname}_${pkgver}.orig.tar.gz)
md5sums=('fbe4d53f2c6fb08519339609f1becffc')

build() {
    cd $srcdir/$pkgname-$pkgver
    ./configure --prefix=/usr --libexecdir=/usr/lib/pidgin-blinklight
    make
}

package() {
    cd $srcdir/$pkgname-$pkgver
    make DESTDIR=$pkgdir install
    rm $pkgdir/usr/lib/purple-2/pidgin-blinklight.la
}
