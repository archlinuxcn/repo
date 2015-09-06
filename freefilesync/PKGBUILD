# Contributor: chenxing <cxcxcxcx AT gmail DOT com>
# Contributor: Michael Burkhard <Michael DOT Burkhard AT web DOT de>
# Maintainer: alexmo82 <25396682 AT live DOT it>

pkgname=freefilesync
pkgver=7.4
pkgrel=1
pkgdesc="Visual folder comparison and synchronization"
arch=('any')
url="http://www.freefilesync.org/"
license=('GPLv3')
depends=(wxgtk webkitgtk2 boost-libs)
makedepends=(boost)
source=(
	"http://downloads.sourceforge.net/project/zenxml/zenXml_2.3.zip"
	"https://www.dropbox.com/s/iwtqvgnmnuiqv9y/FreeFileSync_7.4_Source.zip?dl=0"
	FreeFileSync.desktop 
	ffsicon.png 
	RealtimeSync.desktop 
	rtsicon.png
	)
md5sums=('58baf96cb8e1136d10e1ada7419921c5'
         '37887e3c13c0748949928ecc3ba3974c'
         'a7be7841f47f29d8e6210c8ab592a1e3'
         '1f452dff6f970d95839411008d86250b'
         '90152f1021f2d6fb6ab4fa511dc60fa9'
         'ee5587fa0a8d906ad416564e4daf5a06')


build() {
  echo -n "compiled with  "
  g++ --version
 
 cd ${srcdir}/FreeFileSync/Source
  make launchpad
  
cd RealtimeSync
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