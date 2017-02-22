# Maintainer: Vladimir Kamensky  <mastersoft24@yandex.ru>


pkgname=yandex-browser-beta
pkgver=17.1.1.773_1
pkgrel=1
pkgdesc="The web browser from Yandex.
 Yandex Browser is a browser that combines a minimal design with sophisticated technology to make the web faster, safer, and easier."
arch=('x86_64')
url="http://browser.yandex.ru/beta/"
license=('custom')
categories=('network')

options=(!strip)

depends=('desktop-file-utils' 'gconf' 'alsa-lib'  'gtk2'  'libxkbfile' 'nss' 'libxss' 'libxtst'  )


install='yandex-browser.install'

source=("yandex-browser-beta-$pkgver.deb::http://browser.yandex.ru/download/?beta=1&os=linux&x64=1&package=deb&full=1")
md5sums=("e9f881f17bb911600d2b5645e52947f4")

package() {
	cd "$srcdir"
	
		
	tar -xpJf data.tar.xz
	
	
	cp -r opt usr "$pkgdir"
	
#	if [ ! -a "/usr/lib/libudev.so.0" ]
#	then
#	echo "libudev.so.0 was created"
#	mkdir "$pkgdir/usr/lib"
#	ln -s /usr/lib/libudev.so "$pkgdir/usr/lib/libudev.so.0"
#	fi
	
	#echo 'NOTE: After install run chmod 4755 /opt/yandex/browser-beta/yandex_browser-sandbox as root.'
	
#	mkdir "$pkgdir/usr/share/licenses"	
#	mkdir "$pkgdir/usr/share/licenses/yandex-browser"	
#	cp ../../LICENSE "$pkgdir/usr/share/licenses/yandex-browser"
	
}
