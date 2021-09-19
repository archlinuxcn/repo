# Maintainer: BrainDamage
pkgname="libsixel"
pkgrel=2
pkgver="1.10.1"
pkgdesc="provides a codec for DEC SIXEL graphics, and some converter programs"
arch=("i686" "x86_64")
url="https://github.com/libsixel/libsixel"
license=("MIT")
depends=("libjpeg-turbo" "libpng" "python" "curl" "gdk-pixbuf2" "libbsd")
makedepends=("meson")
sha256sums=('67032a0b9c5a1022308710eb863489dfb9ef685d222106bd8d3e4a3aafa2855c')
source=("https://github.com/libsixel/libsixel/archive/v${pkgver}.tar.gz")

build() {
	meson --prefix=/usr --buildtype=plain -Dtests=enabled -Dlibcurl=enabled -Dgdk-pixbuf2=enabled "${srcdir}/${pkgname}-${pkgver}" build
	meson compile -C build
}

check() {
	meson test -C build
}

package() {
	meson install -C build --destdir "${pkgdir}"
	install -Dm 644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/libsixel/LICENSE"
}
