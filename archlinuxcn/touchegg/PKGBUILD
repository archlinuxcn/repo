# Maintainer: AwesomeHaircut <jesusbalbastro@gmail.com>
# Co-Maintainer: jbouter <aur@kn0x.org>

pkgname=touchegg
pkgver=2.0.12
pkgrel=1
pkgdesc="Multitouch gesture recognizer"
arch=('i686' 'x86_64')
url="https://github.com/JoseExposito/touchegg/"
license=('GPL3')
depends=('libinput' 'cairo' 'systemd-libs' 'libx11' 'libxi' 'libxrandr' 'libxtst' 'pugixml' 'gtk3' 'glib2')
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha512sums=(ee56d81adfced97473f6fcaf641b569aaadc926b613556f8e9b732f95d35c45aa1c18dfab6467d063a5f2e7138960acc115079b458047422a2e8801a4e0a4825)
build() {
	cmake -B build -S "$pkgname-$pkgver" \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-Wno-dev
	make -C build
}

package() {

	make -C build DESTDIR="$pkgdir" install

	[ -d "$pkgdir/lib" ] && mv "$pkgdir/lib" "$pkgdir/usr/lib"

	install -Dm644 "$srcdir/$pkgname-$pkgver/installation/touchegg.desktop" "$pkgdir/etc/xdg/autostart/touchegg.desktop"
}
