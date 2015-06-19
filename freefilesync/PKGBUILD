# Contributor: chenxing <cxcxcxcx AT gmail DOT com>
# Contributor: Michael Burkhard <Michael DOT Burkhard AT web DOT de>
# Maintainer: alexmo82 <25396682 AT live DOT it>

pkgname=freefilesync
pkgver=7.1
pkgrel=0
pkgdesc="Visual folder comparison and synchronization"
arch=('any')
url="http://www.freefilesync.org/"
license=('GPLv3')
depends=(wxgtk webkitgtk2 boost-libs)
makedepends=(boost)
conflicts=(freefilesync-ubuntu)
source=("http://downloads.sourceforge.net/project/zenxml/zenXml_2.2.zip"
	"http://sourceforge.net/projects/freefilesync/files/FreeFileSync/${pkgver}/FreeFileSync_${pkgver}_Source.zip"	
	FreeFileSync.desktop 
	ffsicon.png 
	RealtimeSync.desktop 
	rtsicon.png)
md5sums=('4c1f953b789d6dcbcb7eccab3d33e8ac'
         '41ece189e94358d75de3619455601e90'
         'a7be7841f47f29d8e6210c8ab592a1e3'
         '1f452dff6f970d95839411008d86250b'
         '90152f1021f2d6fb6ab4fa511dc60fa9'
         'ee5587fa0a8d906ad416564e4daf5a06')

build() {
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