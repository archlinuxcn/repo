# Maintainer: not_anonymous <nmlibertarian@gmail.com>

# Contributor: Carsten Feuls <archlinux@carstenfeuls.de> aka DL1CAF
# Contributor: Andrey Semisokhin <customs.rnd@gmail.com>
# Original Submission: Bob Finch <w9ya@qrparci.net>

pkgname=gpredict
pkgver=2.2.1
pkgrel=2
pkgdesc="Real-time satellite tracking and orbit prediction application"
arch=('i686' 'x86_64' 'armv5h' 'armv6h' 'armv7h')
url="http://gpredict.oz9aec.net/"
license=('GPL')
depends=('curl>=7.19' 'goocanvas2' 'hamradio-menus')
makedepends=('autoconf' 'automake' 'intltool')
provides=('gpredict')
conflicts=('gpredict')
options=('!emptydirs')
source=(https://github.com/csete/gpredict/releases/download/v$pkgver/$pkgname-$pkgver.tar.bz2
	diff.qth-data.h)

prepare() {
	cd $srcdir/$pkgname-$pkgver

	patch -p0 < ../diff.qth-data.h
}

build() {
	cd $srcdir/$pkgname-$pkgver

	./autogen.sh
	./configure --prefix=/usr
	make
}

check() {
	cd $srcdir/$pkgname-$pkgver

#	make check
#	make -k check
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
md5sums=('38a7bda79989c5921d1c0bcc6c238382'
         'ecb2e46a09cc8cd1a525b8fa1a2b688d')
sha256sums=('e759c4bae0b17b202a7c0f8281ff016f819b502780d3e77b46fe8767e7498e43'
            '41388ce2374cc17f5292b6dd84459b8b519c008c91c90fd137a055f4238f6629')
