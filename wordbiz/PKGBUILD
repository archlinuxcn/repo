# Maintainer: colinkeenan at gmail dot com
pkgname=wordbiz
pkgver=1.8.7
pkgrel=2
pkgdesc="Internet Scrabble Club client"
arch=("x86_64" "i686")
url="http://www.isc.ro"
license=("unknown")
depends=("java-runtime")
source=("http://www.isc.ro/linux/WordBiz18linux.zip" 
        "https://raw.githubusercontent.com/colinkeenan/archpkg-${pkgname}/v${pkgver}/wordbiz" 
	"https://raw.githubusercontent.com/colinkeenan/archpkg-${pkgname}/v${pkgver}/wordbiz.desktop")
md5sums=('dd3c078f758196606e21430ac248b8d5'
         '21544a9059d8d55dbdb24511fac98644'
         '5b868fccffb9d25671bdd4d0175e9ea9')

package() {	
	for file in $(find WordBiz -type f); do
	    install -m 644 -D ${file} $pkgdir/opt/WordBiz/${file#WordBiz/}
	done
	install -m755 -D wordbiz $pkgdir/usr/bin/wordbiz
	install -m644 -D wordbiz.desktop $pkgdir/usr/share/applications/wordbiz.desktop
}
