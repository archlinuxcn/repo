# Maintainer: not_anonymous <nmlibertarian@gmail.com>
# Previous Maintainer: Wijnand Modderman-Lenstra <maze@maze.io>
# Original Submission: Bob Finch <w9ya@qrparci.net>

pkgname=trustedqsl
__pkgname=tqsl
pkgver=2.6.5
pkgrel=2
pkgdesc="QSO log signing data for the ARRL Logbook of The World (LoTW)"
arch=('i686' 'x86_64' 'aarch64')
url="http://lotw.arrl.org/"
license=('custom:ARRL')
depends=('lmdb' 'wxgtk3' 'hamradio-menus')
makedepends=('cmake' 'libxxf86vm')
provides=('tqsllib' 'trustedqsl')
conflicts=('trustedqsl-git')
replaces=('tqsl')
source=(http://www.arrl.org/$__pkgname/$__pkgname-$pkgver.tar.gz
	$pkgname.desktop)

build() {
	cd "$srcdir/${__pkgname}-$pkgver"

	mkdir -p build
	cd build
	cmake \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DwxWidgets_CONFIG_EXECUTABLE='/usr/bin/wx-config' \
		-DwxWidgets_wxrc_EXECUTABLE='/usr/bin/wxrc' \
		../
	make
}

package() {
	cd "$srcdir/${__pkgname}-$pkgver/build"
	make DESTDIR="$pkgdir/" install

	find "$pkgdir" -name wxstd* -exec rm {} +

	install -D -m644 "../LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.txt"

	mkdir -p $pkgdir/usr/share/applications
	install -D -m 644 ../../$pkgname.desktop $pkgdir/usr/share/applications

	rm -rf $pkgdir/usr/include $pkgdir/man5
}
md5sums=('dd07f9d9000949937d73fe0ce1b7956c'
         '6dd4296f5fda2d77922c9cbe4a120d3b')
sha256sums=('5063cca759806ab1d6b8b6d9bb6c16a6380275ff192a3d0cc24aa9df6539ffcc'
            '68129b7f7ddbb75be52f1b9164d43c6d9805c5877423546b50397c2d920c79e9')
