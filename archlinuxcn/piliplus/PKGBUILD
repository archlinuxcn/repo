# Maintainer: George Hu <integral@archlinux.org>

pkgname=piliplus
_srcname=PiliPlus
pkgver=1.1.4.15
pkgrel=1
pkgdesc="A third-party Bilibili client developed in Flutter"
url="https://github.com/bggRGjQaUbCoE/${_srcname}"
license=('GPL-3.0-or-later')
arch=('x86_64')
depends=('gtk3' 'mpv' 'libayatana-appindicator')
makedepends=('git' 'clang' 'cmake' 'ninja' 'fvm' 'patchelf')
source=("git+${url}.git#tag=${pkgver}")
sha256sums=('6232e4c6ecaa5db71b1a1c44f694a20873171817fb24be0f3f3e1897adb1f114')

prepare() {
	cd "${_srcname}/"
	fvm install
	fvm flutter --disable-analytics
	fvm flutter --no-version-check pub get
}

build() (
	cd "${_srcname}/"
	fvm flutter build linux --no-pub --release \
		--dart-define pili.name="${pkgver}" \
		--dart-define pili.code="$(git rev-list --count HEAD)" \
		--dart-define pili.hash="$(git rev-parse HEAD)" \
		--dart-define pili.time="$(date +%s)"
)

package() {
	cd "${_srcname}/"

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

	cd assets
	install -Dm644 images/logo/logo.png "${pkgdir}/usr/share/icons/hicolor/512x512/apps/${pkgname}.png"
	install -Dm644 "linux/${pkgname}.desktop" -t "${pkgdir}/usr/share/applications/"
}
