# Maintainer: not_anonymous <nmlibertarian@gmail.com>

# Contributor: Carsten Feuls <archlinux@carstenfeuls.de> aka DL1CAF
# Contributor: Andrey Semisokhin <customs.rnd@gmail.com>
# Original Submission: Bob Finch <w9ya@qrparci.net>

pkgname=gpredict
pkgver=2.5.1
pkgrel=1
pkgdesc="Real-time satellite tracking and orbit prediction application"
arch=('i686' 'x86_64' 'armv5h' 'armv6h' 'armv7h' 'aarch64')
url="http://gpredict.oz9aec.net/"
license=('GPL-2.0-only')
depends=('curl>=7.19' 'goocanvas2' 'hamradio-menus')
makedepends=('autoconf' 'automake' 'intltool')
provides=('gpredict')
conflicts=('gpredict')
options=('!emptydirs')
source=(https://github.com/csete/gpredict/releases/download/v$pkgver/$pkgname-$pkgver.tar.bz2)

build() {
	cd $srcdir/$pkgname-$pkgver

	autoreconf -vfi -I /usr/share/gettext/m4
	./configure --prefix=/usr
	make
}

check() {
	cd $srcdir/$pkgname-$pkgver

	make -i check
}
	
package()
{
	cd $srcdir/$pkgname-$pkgver

	make DESTDIR=$pkgdir install

	rm -rf $pkgdir/usr/share/$pkgname/COPYING

	sed -i '$ a\X-DCOP-ServiceType=none' $pkgdir/usr/share/applications/$pkgname.desktop
	sed -i '$ a\X-KDE-SubstituteUID=false' $pkgdir/usr/share/applications/$pkgname.desktop
}
md5sums=('c6acc86f9a0bf3eb8673557775e13604')
sha256sums=('c26ff5f9bfe9468bd48426dac4782f860c208960b0551feba3e38e364fbcd797')
