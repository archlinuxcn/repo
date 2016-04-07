# Maintainer: Alfonso Saavedra "Son Link" <sonlink.dourden@gmail.com>
pkgname=megasync
pkgver=2.8.0
pkgrel=1
pkgdesc="Sync your files to your Mega account. Official app"
arch=('i686' 'x86_64')
url="https://mega.nz/#sync"
license=('custom:MEGA LIMITED CODE REVIEW LICENCE')
conflicts=('megatools')
depends=('openssl' 'c-ares' 'libgcrypt' 'crypto++' 'qt4' 'libpng' 'qtchooser' 'sqlite' 'libuv')
makedepends=('git')
optdepends=('sni-qt: fix systray issue on KDE and LXQt')
source=("git+https://github.com/meganz/MEGAsync.git#commit=cf855e49c945860a90d91fe67767956dcbeb923d"
        "git+https://github.com/meganz/sdk.git#commit=4ed589a68fdd3d9b170aef78b18c4c5753bb3f8f"
	"megasync.install")
md5sums=('SKIP'
         'SKIP'
	'cf6fbb67643cc68baa8ea89bbd989fa0')
install="${pkgname}.install"

prepare(){
	cd MEGAsync
  	git submodule init
  	git config submodule.src/MEGASync/mega.url "$srcdir/sdk"
  	git submodule update
}

build(){
	cd MEGAsync/src/MEGASync/mega
  	./autogen.sh
  	./configure \
		--disable-silent-rules \
 		--disable-curl-checks \
		--disable-megaapi \
		--with-cryptopp \
		--without-sodium \
		--with-zlib \
		--with-sqlite \
		--with-cares \
		--with-curl \
		--without-freeimage \
		--without-readline \
		--without-termcap \
		--disable-posix-threads \
		--disable-examples \
		--prefix=/usr
 
	cd ../..
	qmake-qt4 CONFIG+="release" MEGA.pro
	lrelease-qt4 MEGASync/MEGASync.pro
	make
}

package (){
	cd MEGAsync
	install -Dm 644 LICENCE.md $pkgdir/usr/share/licenses/megasync/LICENCE.md
	install -Dm 644 installer/terms.txt $pkgdir/usr/share/licenses/megasync/terms.txt
 
	cd src/MEGASync
	install -Dm 755 megasync $pkgdir/usr/bin/megasync

	cd platform/linux/data
	install -Dm 644 megasync.desktop $pkgdir/usr/share/applications/megasync.desktop
	
	cd icons/hicolor
	for size in 16x16 32x32 48x48 128x128 256x256
	do
		install -Dm 644 $size/apps/mega.png $pkgdir/usr/share/icons/hicolor/$size/apps/mega.png
	done
}
