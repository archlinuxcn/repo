pkgname=115wangpan
pkgver=4.0.1
pkgrel=1
pkgdesc='The 115 Wangpan client'
arch=('x86_64' 'i686')
url='http://pc.115.com/linux.html'
license=('unknown')
if test "$CARCH" == x86_64; then
	depends=('lib32-libx11' 'lib32-gcc-libs')
elif test "$CARCH" == i686; then
	depends=('libx11')
fi
source=("http://pc.115.com/download/linux/115yun_linux_v${pkgver}.deb")
sha1sums=('66c74d7fd69bd86de52da66a41883156ba0c3e40')

build(){
	cd ${srcdir}
	tar xvf data.tar.gz
}

package(){
	install -dm755 ${pkgdir}/usr/lib
	cp -r ${srcdir}/lib/fonts ${pkgdir}/usr/lib
	install -dm755 ${pkgdir}/usr/share/115wangpan
	install -Dm755 ${srcdir}/usr/bin/115pan ${srcdir}/usr/bin/qt.conf ${pkgdir}/usr/share/115wangpan
	install -dm755 ${pkgdir}/usr/bin
	ln -s /usr/share/115wangpan/115pan ${pkgdir}/usr/bin/115pan
	install -dm755 ${pkgdir}/usr/share/pixmaps
	cp ${srcdir}/usr/share/pixmaps/115pan.png ${pkgdir}/usr/share/pixmaps
	install -dm755 ${pkgdir}/usr/share/applications
	cp ${srcdir}/usr/share/applications/115pan.desktop ${pkgdir}/usr/share/applications
}
