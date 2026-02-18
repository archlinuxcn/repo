# Maintainer: Integral <integral@archlinuxcn.org>
# Contributor: Uncore <contactuncor3@gmail.com>

pkgname=idescriptor
_srcname=iDescriptor
pkgver=0.3.0
pkgrel=1
pkgdesc="A free, open-source, and cross-platform iDevice management tool"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/${_srcname}/${_srcname}"
license=('AGPL-3.0-or-later')
depends=(
	'libimobiledevice>=1.4.0'
	'libtatsu>=1.0.5'
	'libimobiledevice-glue'
	'libirecovery'
	'libplist'
	'usbmuxd'
	'libusbmuxd'
	'openssl'
	'libssh'
	'libusb'
	'pugixml'
	'qrencode'
	'libheif'
	'libzip'
	'qt6-base'
	'qt6-multimedia'
	'qt6-declarative'
	'qt6-serialport'
	'qt6-positioning'
	'qt6-location'
	'qtermwidget'
	'avahi'
	'libsecret'
	'gnome-keyring'
	'ffmpeg'
	'ifuse'
	'gstreamer'
	'gst-plugins-base-libs'
	'gst-plugins-good'
	'gst-plugins-bad'
	'gst-plugins-ugly'
	'gst-libav'
)
makedepends=('git' 'cmake' 'go')
source=("git+${url}.git#tag=v${pkgver}"
	"git+https://github.com/iDescriptor/uxplay.git"
	"git+https://github.com/uncor3/libipatool-go.git"
	"git+https://github.com/libZQT/ZUpdater.git")
sha256sums=('8f77628776d3f32cfa76bb77dfed37e0f72ea6cee43276dfef9c5c2b62c3736c'
            'SKIP'
            'SKIP'
            'SKIP')

prepare() {
	cd "${_srcname}/"
	git rm lib/win-ifuse

	git submodule init
	git config submodule.lib/uxplay.url "${srcdir}/uxplay"
	git config submodule.lib/ipatool-go.url "${srcdir}/libipatool-go"
	git config submodule.lib/zupdater.url "${srcdir}/ZUpdater"
	git -c protocol.file.allow=always submodule update

	cd lib/ipatool-go
	export GOPATH="${srcdir}"
	go mod download -modcacherw -x
}

build() {
	local cmake_options=(
		-B build
		-S "${_srcname}"
		-D CMAKE_BUILD_TYPE=None
		-D CMAKE_INSTALL_PREFIX=/usr
		-D PACKAGE_MANAGER_MANAGED=ON
		-D ENABLE_RECOVERY_DEVICE_SUPPORT=ON
		-D NO_MARCH_NATIVE=ON
	)

	cmake "${cmake_options[@]}"
	cmake --build build
}

package() {
	DESTDIR="${pkgdir}" cmake --install build
}
