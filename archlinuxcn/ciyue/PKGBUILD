# Maintainer: Integral <integral@member.fsf.org>

pkgname=ciyue
_srcname=Ciyue
pkgver=1.21.0
pkgrel=1
pkgdesc="A simple mdict dictionary with Android/Windows/Linux support"
url="https://mumulhl.eu.org/${_srcname}"
license=('MIT')
arch=('x86_64')
depends=('gtk3' 'gstreamer' 'gst-plugins-base' 'libkeybinder3' 'libayatana-appindicator')
makedepends=('clang' 'cmake' 'ninja' 'fvm' 'patchelf')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/mumu-lhl/${_srcname}/archive/refs/tags/v${pkgver}.tar.gz"
	"${pkgname}.desktop")
sha256sums=('861444561ddcc29dae2eb8c283e9801367afb62599b34a68b9c0b745cead8f17'
            '5a6214e368452ed4be188b7e74395f7f0e34f3101d109b7e814d6ac0a291b1cc')

prepare() {
	cd "${_srcname}-${pkgver}/"
	fvm install stable
	fvm use stable -f
	fvm flutter --disable-analytics
	fvm flutter --no-version-check pub get
}

build() (
	cd "${_srcname}-${pkgver}/"
	fvm flutter build linux --no-pub --release
)

package() {
	cd "${_srcname}-${pkgver}/"

	pushd build/linux/x64/release
	install -Dm755 "bundle/${pkgname}" -t "${pkgdir}/usr/lib/${pkgname}/"
	cmake -DCMAKE_INSTALL_PREFIX="${pkgdir}/usr/lib/${pkgname}" .
	cmake -P cmake_install.cmake
	popd

	# Reset RUNPATH
	patchelf --set-rpath '$ORIGIN' ${pkgdir}/usr/lib/${pkgname}/lib/*.so

	# Symlink
	install -dm755 "${pkgdir}/usr/bin"
	ln -s "/usr/lib/${pkgname}/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"

	# Icon
	install -Dm644 assets/icon.png "${pkgdir}/usr/share/icons/hicolor/512x512/apps/${pkgname}.png"

	# Desktop Launcher
	install -Dm644 "${srcdir}/${pkgname}.desktop" -t "${pkgdir}/usr/share/applications/"

	# License
	install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}
