# Maintainer: Frederik Schwan <frederik dot schwan at linux dot com>
# Contributor: Felix Yan <felixonmars@gmail.com>
# Contributor: kiefer <jorgelmadrid@gmail.com>
# Contributor: Alessio Sergi <asergi at archlinux dot us>
# Contributor: Gaute Hope <eg@gaute.vetsj.com>
# Contributor: Marcos Heredia <chelqo@gmail.com>
 
pkgname=gtkhotkey
pkgver=0.2.1
pkgrel=9
pkgdesc="Platform independent hotkey handling for Gtk+ applications"
arch=('i686' 'x86_64')
url="https://launchpad.net/gtkhotkey"
license=('LGPL3')
depends=('gtk2')
makedepends=('intltool')
source=("http://launchpad.net/$pkgname/0.2/$pkgver/+download/$pkgname-$pkgver.tar.gz")
md5sums=('bfdc73e68e9adbe0d506d31a25862914')
 
build() {
  cd "$srcdir/$pkgname-$pkgver"
 
  # doc path fix
  sed -i '/gtkhotkeydocdir/s/\${prefix}/\${datadir}/g' Makefile.{am,in}
 
  # glib2 fix
  sed -i 's|glib/gquark\.h|glib.h|' src/gtk-hotkey-error.h
  sed -i 's|glib/gtypes\.h|glib.h|' src/x11/tomboykeybinder.h
 
  ./configure --prefix=/usr \
              --disable-static
  make
}
 
package() {
  cd "$srcdir/$pkgname-$pkgver"
 
  make DESTDIR="$pkgdir/" install
}
