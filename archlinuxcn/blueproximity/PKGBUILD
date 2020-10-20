# Maintainer: Erhad Husovic <xdaemonx@protonmail.ch>
# Contributor: Andre Schlichting <andre dot schlichting at googlemail dot com>
# Contributor: Manuel "ekerazha" C. (www.ekerazha.com)

pkgname=blueproximity
pkgver=1.2.5
pkgrel=9
pkgdesc="A proximity detector for your mobile phone via bluetooth."
arch=('i686' 'x86_64')
url="http://sourceforge.net/projects/blueproximity/"
license=('GPL')
depends=('bluez-utils-compat' 'pygtk' 'python2-configobj>=4.7.0-1' 'python2-pybluez>=0.14-2' 'python2' 'librsvg')
optdepends=('gnome-screensaver' 'xscreensaver')
source=(http://download.sourceforge.net/sourceforge/blueproximity/$pkgname-$pkgver.tar.gz \
	blueproximity.desktop blueproximity.xpm blueproximity-1.2.5.orig.patch)
options=(emptydirs)
md5sums=('5fa33a73869d1b6f40957bdba3da636b'
         '1e08ef00fc87ccd5ab78f893efa8ff2d'
         '1e2f0204a6a54bee5b5263cb0f5cd8f0'
         '8c42f275aaa26a22df690bccac3ad7be')

build() {
  rm $srcdir/$pkgname-$pkgver.orig/ChangeLog
  rm $srcdir/$pkgname-$pkgver.orig/COPYING
  rm $srcdir/$pkgname-$pkgver.orig/README
  rm -r $srcdir/$pkgname-$pkgver.orig/doc

  cd $srcdir/$pkgname-$pkgver.orig/

  patch -p1 -i ../$pkgname-$pkgver.orig.patch || return 1
}

package() {
  mkdir -p $pkgdir/usr/bin
  mkdir -p $pkgdir/usr/share/applications
  mkdir -p $pkgdir/usr/share/$pkgname
  mkdir -p $pkgdir/usr/share/pixmaps

  install -D -m755 $srcdir/$pkgname-$pkgver.orig/proximity.py $pkgdir/usr/bin/
  install -D -m755 $srcdir/$pkgname-$pkgver.orig/start_proximity.sh $pkgdir/usr/bin/
  install -D -m644 $srcdir/blueproximity.desktop $pkgdir/usr/share/applications/
  install -D -m644 $srcdir/blueproximity.xpm $pkgdir/usr/share/pixmaps/
  cp -r $srcdir/$pkgname-$pkgver.orig/* $pkgdir/usr/share/$pkgname/
  chmod -R 644 $pkgdir/usr/share/$pkgname/*

  sed -i -e "s|dist_path = './'|dist_path = '/usr/share/blueproximity/'|g" $pkgdir/usr/bin/proximity.py
}
