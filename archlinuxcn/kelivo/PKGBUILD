# Maintainer: George Hu <integral@archlinux.org>

pkgname=kelivo
pkgver=1.1.11
pkgrel=1
pkgdesc="A Flutter LLM Chat Client"
arch=('x86_64')
url="https://${pkgname}.psycheas.top"
license=('AGPL-3.0-only')
depends=(
	'at-spi2-core'
	'cairo'
	'fontconfig'
	'gdk-pixbuf2'
	'glib2'
	'glibc'
	'gst-plugins-base-libs'
	'gstreamer'
	'gtk3'
	'hicolor-icon-theme'
	'libappindicator'
	'libepoxy'
	'libgcc'
	'libkeybinder3'
	'libstdc++'
	'pango'
)
makedepends=('clang' 'cmake' 'fvm' 'imagemagick' 'ninja' 'patchelf')
source=(
	"${pkgname}-${pkgver}.tar.gz::https://github.com/Chevey339/${pkgname}/archive/v${pkgver}.tar.gz"
	"com.psyche.${pkgname}.desktop"
)
sha256sums=('707f346cbd4ccbcbf91dbf9cfb3ef3a92decfd1b7bbb09de55e2b2b2bb6016fd'
            'ecae7320d7a984c40804ff8c3e075ce45ff302052f94ba61abc1103b825f6bcd')

prepare() {
	cd "${pkgname}-${pkgver}/"
	fvm install stable
	fvm use stable
	fvm flutter --disable-analytics
	fvm flutter --no-version-check pub get
}

build() (
	cd "${pkgname}-${pkgver}/"
	CXXFLAGS+=" -Wno-error=sometimes-uninitialized" fvm flutter build linux --no-pub --release
)

package() {
	cd "${pkgname}-${pkgver}/"

	pushd build/linux/x64/release
	install -Dm755 "bundle/${pkgname}" -t "${pkgdir}/usr/lib/${pkgname}/"
	cmake -DCMAKE_INSTALL_PREFIX="${pkgdir}/usr/lib/${pkgname}" .
	cmake -P cmake_install.cmake
	popd

	# Reset RPATH
	patchelf --set-rpath '$ORIGIN' ${pkgdir}/usr/lib/${pkgname}/lib/*.so

	# Symlink
	install -dm755 "${pkgdir}/usr/bin"
	ln -s "/usr/lib/${pkgname}/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"

	install -Dm644 "${srcdir}/com.psyche.${pkgname}.desktop" -t "${pkgdir}/usr/share/applications/"

	cd assets
	for r in 16 24 32 48 64 128 256 512; do
		install -Dm644 <(magick app_icon.png -resize "${r}x${r}" -) "${pkgdir}/usr/share/icons/hicolor/${r}x${r}/apps/${pkgname}.png"
	done
}
