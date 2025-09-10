# Maintainer: Integral <integral@member.fsf.org>

pkgname=danxi
pkgver=1.4.8
pkgrel=1
pkgdesc="Maybe the best all-rounded service app for Fudan University students | 可能是复旦学生最好的第三方校园服务 APP"
url="https://github.com/DanXi-Dev/DanXi"
license=('GPL-3.0-or-later')
arch=('x86_64')
depends=('gtk3' 'libsecret' 'gnome-keyring')
makedepends=('git' 'clang' 'cmake' 'ninja' 'fvm' 'imagemagick')
source=("git+${url}.git#tag=v${pkgver}")
sha256sums=('24bc79baf3a9eda79dc0e768e104b5a608f4a0a73c4e7bc26d9bbdde0969f1f9')

prepare() {
	cd DanXi
	fvm install stable
	fvm use stable
	fvm flutter --disable-analytics
	fvm flutter --no-version-check pub get
}

build() (
	cd DanXi
	export CXXFLAGS+=" -Wno-error=unused-result"
	fvm dart --disable-analytics
	fvm dart run intl_utils:generate
	fvm dart build_release.dart --target linux --versionCode dummy
)

package() {
	cd DanXi

	pushd build/linux/x64/release
	install -Dm755 bundle/dan_xi -t "${pkgdir}/usr/lib/${pkgname}/"
	cmake -DCMAKE_INSTALL_PREFIX="${pkgdir}/usr/lib/${pkgname}" .
	cmake -P cmake_install.cmake
	popd

	# Symlink
	install -dm755 "${pkgdir}/usr/bin"
	ln -s "/usr/lib/${pkgname}/dan_xi" "${pkgdir}/usr/bin/dan_xi"

	# Icon
	for r in 16 24 32 48 64 128 256 512; do
		install -dm755 "${pkgdir}/usr/share/icons/hicolor/${r}x${r}/apps/"
		magick packaging/dan_xi.png -resize "${r}x${r}" "${pkgdir}/usr/share/icons/hicolor/${r}x${r}/apps/dan_xi.png"
	done

	# Desktop Launcher
	install -Dm644 "packaging/io.github.danxi_dev.dan_xi.desktop" "${pkgdir}/usr/share/applications/dan_xi.desktop"
}
