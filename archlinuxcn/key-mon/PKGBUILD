# Maintainer: Lara Maia <lara@craft.net.br>
#
# Contributors: Nuno Araujo <nuno.araujo at russo79.com>
#               Guan Qing <neokuno@gmail.com>
#               Liudas <liudas@akmc.lt>
#               Tom Tryfonidis <tomtryf [at] gmail [dot] com>

pkgname=key-mon
pkgver=1.17
pkgrel=1
pkgdesc="A small utility to display your current keyboard and mouse status. Useful for screencasts."
arch=('any')
url="http://code.google.com/p/key-mon/"
depends=('pygtk' 'dbus-glib' 'python2-dbus' 'python2-xlib')
makedepends=('python2-distribute')
install=${pkgname}.install
license=('Apache 2.0')

source=(https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/$pkgname/$pkgname-$pkgver.tar.gz
        $pkgname.install)
        
md5sums=('68bfe1ff8765878cf7d100759d433473'
         'bb92b6ada97430e35595ca0f7e48b931')

package() {
  cd "$srcdir"/$pkgname-$pkgver

  python2 setup.py install --root="$pkgdir"
  
  install -Dm644 "$srcdir"/$pkgname-$pkgver/icons/key-mon.desktop "$pkgdir"/usr/share/applications/key-mon.desktop
  install -Dm644 "$srcdir"/$pkgname-$pkgver/icons/key-mon.xpm "$pkgdir"/usr/share/pixmaps/key-mon.xpm

  find "$pkgdir" -type f -exec sed -i 's|/usr/bin/python$|/usr/bin/python2|g' {} +
}








