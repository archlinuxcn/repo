# Maintainer: grufo <madmurphy333 AT gmail DOT com>

pkgname='nautilus-checksums'
pkgver='0.1.0'
pkgrel=1
pkgdesc='Add checksums to Nautilus'\'' properties window'
arch=('i686' 'x86_64')
url="https://gitlab.gnome.org/madmurphy/${pkgname}"
license=('GPL')
depends=('glib2' 'libnautilus-extension')
conflicts=("${pkgname}-git" "${pkgname}-bin")
source=("https://github.com/madmurphy/${pkgname}/releases/download/${pkgver}/${pkgname}-${pkgver}-with-configure.tar.gz")
install="${pkgname}.install"
sha256sums=('46b717eaa24b95f77b74a0635cb76f70e15bd5072362545f66f94e33db89bbcf')

build() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	./configure --prefix=/usr
	make
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	make DESTDIR="${pkgdir}" install
}

