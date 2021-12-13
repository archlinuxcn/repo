# Maintainer: BrainDamage
pkgname="libsixel"
pkgrel=4
pkgver="1.10.3"
pkgdesc="provides a codec for DEC SIXEL graphics, and some converter programs"
arch=("i686" "x86_64")
url="https://github.com/libsixel/libsixel"
license=("MIT")
depends=("libjpeg-turbo" "libpng" "python" "curl" "gdk-pixbuf2" )
makedepends=("meson")
sha256sums=('028552eb8f2a37c6effda88ee5e8f6d87b5d9601182ddec784a9728865f821e0')
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
	install -Dvm 644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
