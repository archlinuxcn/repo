# Maintainer: Integral <integral@member.fsf.org>

pkgname=kazumi
_srcname=Kazumi
pkgver=1.7.9
pkgrel=1
pkgdesc="基于自定义规则的番剧采集APP，支持流媒体在线观看，支持弹幕"
url="https://github.com/Predidit/Kazumi"
license=('GPL-3.0-or-later')
arch=('x86_64')
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
)
makedepends=('clang' 'cmake' 'ninja' 'fvm')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('21e8748499f94a49075c394418f72c64275fd1f8feba0e4ca60680f5636b6c4f')

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

	install -dm755 "${pkgdir}/usr/bin"
	ln -s "/usr/lib/${pkgname}/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"

	local _app_id="io.github.Predidit.Kazumi"
	install -Dm644 "assets/images/logo/logo_linux.png" "${pkgdir}/usr/share/icons/hicolor/512x512/apps/${_app_id}.png"
	install -Dm644 "assets/linux/${_app_id}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
}
