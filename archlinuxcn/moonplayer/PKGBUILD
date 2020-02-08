# maintainer: hzy068808 at gmail.com
# contributer: a304yuanyuan at gmail.com
# contributer: rob.til.freedman@googlemail.com

pkgname=moonplayer
pkgver=3.1
pkgrel=1
pkgdesc="A qt font-end for mplayer with the abilities of watching and downloading videos from chinese network"
arch=('i686' 'x86_64')
url="https://github.com/coslyk/moonplayer"
license=('GPL')
depends=('python' 'qt5-x11extras' 'qt5-base' 'qt5-declarative' 'qt5-quickcontrols' 'qt5-quickcontrols2' 'mpv')
makedepends=('cmake' 'git' 'qt5-tools')
source=(
	$pkgname-$pkgver.tar.gz::https://github.com/coslyk/moonplayer/archive/v$pkgver.tar.gz
	)
sha1sums=('f8b571b8fb076b0f16be00ca68ab20ea9911eddc')

build() {
	cd $srcdir/$pkgname-$pkgver
  mkdir build
  cd build

  cmake .. -DCMAKE_INSTALL_PREFIX=/usr

	make
}

package() {
	cd $srcdir/$pkgname-$pkgver/build

	make DESTDIR="${pkgdir}" install

	#clean pyc
	#rm $pkgdir/usr/share/moonplayer/plugins/*.pyc

	cd $pkgdir/usr/share

	mv icons pixmaps
}
