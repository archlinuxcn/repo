# Contributor: chenxing <cxcxcxcx AT gmail DOT com>
# Contributor: Michael Burkhard <Michael DOT Burkhard AT web DOT de>
# Maintainer: alexmo82 <25396682 AT live DOT it>

pkgname=freefilesync
pkgver=7.5
pkgrel=0
pkgdesc="Visual folder comparison and synchronization"
arch=('any')
url="http://www.freefilesync.org/"
license=('GPLv3')
depends=(wxgtk webkitgtk2 boost-libs)
makedepends=(boost)
source=("http://downloads.sourceforge.net/project/zenxml/zenXml_2.3.zip"
	"FreeFileSync_${pkgver}_Source.zip::https://db.tt/46y42Ic0"
	FreeFileSync.desktop
	ffsicon.png
	RealtimeSync.desktop
	rtsicon.png)
md5sums=('58baf96cb8e1136d10e1ada7419921c5'	#zen
         '404695994e45758a4bdf0ebcc0956d01'	#ffs
         'a7be7841f47f29d8e6210c8ab592a1e3'
         '1f452dff6f970d95839411008d86250b'
         '90152f1021f2d6fb6ab4fa511dc60fa9'
         'ee5587fa0a8d906ad416564e4daf5a06')


build() {
  echo -n "compiled with  "
  g++ --version			# just in case of compile errors
 
  cd ${srcdir}/FreeFileSync/Source
  sed -i 's/-std=c++11/-std=c++14/' Makefile
  make launchpad
  
  cd RealtimeSync
  sed -i 's/-std=c++11/-std=c++14/' Makefile
  make launchpad
}

package() {
  cd ${srcdir}/FreeFileSync/Source
  make DESTDIR=${pkgdir} install

  cd RealtimeSync
  make DESTDIR=${pkgdir} install

  cd ${srcdir}
  install -Dm644 FreeFileSync.desktop $pkgdir/usr/share/applications/FreeFileSync.desktop
  install -Dm644 ffsicon.png $pkgdir/usr/share/pixmaps/ffsicon.png
  install -Dm644 RealtimeSync.desktop $pkgdir/usr/share/applications/RealtimeSync.desktop
  install -Dm644 rtsicon.png $pkgdir/usr/share/pixmaps/rtsicon.png
}