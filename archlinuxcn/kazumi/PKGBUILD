# Maintainer: Integral <integral@member.fsf.org>

pkgname=kazumi
_srcname=Kazumi
pkgver=1.9.2
pkgrel=2
pkgdesc="基于自定义规则的番剧采集APP，支持流媒体在线观看，支持弹幕"
url="https://${pkgname}.app"
license=('GPL-3.0-or-later')
arch=('x86_64' 'aarch64')
depends=(
	'gtk3'
	'webkit2gtk-4.1'
	'libayatana-appindicator'
	'xdg-user-dirs'
	'alsa-lib'
	'libvdpau'
	'libpulse'
	'libxss'
	'libarchive'
	'libcdio'
	'libcdio-paranoia'
	'libdvdnav'
)
makedepends=('clang' 'cmake' 'ninja' 'fvm' 'patchelf')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/Predidit/${_srcname}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('77c81e94eeadb4b3bee27c78c84f253fca28ae1c122534d6f74a9ad0c9a55c3d')

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

	case "${CARCH}" in
	"x86_64") local _dartarch="x64" ;;
	"aarch64") local _dartarch="arm64" ;;
	esac

	pushd "build/linux/${_dartarch}/release/"
	install -Dm755 "bundle/${pkgname}" -t "${pkgdir}/usr/lib/${pkgname}/"
	cmake -DCMAKE_INSTALL_PREFIX="${pkgdir}/usr/lib/${pkgname}" .
	cmake -P cmake_install.cmake
	popd

	patchelf --set-rpath '$ORIGIN' ${pkgdir}/usr/lib/${pkgname}/lib/*.so

	install -dm755 "${pkgdir}/usr/bin"
	ln -s "/usr/lib/${pkgname}/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"

	local _app_id="io.github.Predidit.Kazumi"
	install -Dm644 "assets/images/logo/logo_linux.png" "${pkgdir}/usr/share/icons/hicolor/512x512/apps/${_app_id}.png"
	install -Dm644 "assets/linux/${_app_id}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
}
