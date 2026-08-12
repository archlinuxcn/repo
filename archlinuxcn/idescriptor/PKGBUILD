# Maintainer: Integral <integral@archlinuxcn.org>
# Contributor: Uncore <contactuncor3@gmail.com>

pkgname=idescriptor
_srcname=iDescriptor
pkgver=0.6.1
pkgrel=1
pkgdesc="A free, open-source, and cross-platform iDevice management tool"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/${_srcname}/${_srcname}"
license=('AGPL-3.0-or-later')
depends=(
	'libplist'
	'usbmuxd'
	'libusbmuxd'
	'openssl'
	'libssh'
	'libusb'
	'libheif'
	'libzip'
	'qt6-base'
	'qt6-multimedia'
	'qt6-declarative'
	'qt6-serialport'
	'qt6-positioning'
	'qt6-location'
	'avahi'
	'libsecret'
	'org.freedesktop.secrets'
	'ffmpeg'
	'gstreamer'
	'gst-plugins-base-libs'
	'qt6-declarative'
	'qt6-5compat'
	'qt6-multimedia'
	'qt6-svg'
	'gst-plugin-qmlgl'
	'gst-plugin-qml6'
	'gst-plugins-good'
	'gst-plugins-bad'
	'gst-libav'
	'hicolor-icon-theme'
	'sqlite'
)
optdepends=('ifuse: use ifuse provided by libimobiledevice instead of Rust implementation')
makedepends=('git' 'cargo' 'cmake')
source=("git+${url}.git#tag=v${pkgver}"
	"git+https://github.com/iDescriptor/uxplay.git"
	"git+https://github.com/uncor3/idevice.git")
sha256sums=('e3bacca4647f927a0f7772c51fe46b45dac9c5d321f95d459d6e6549dc1d539d'
            'SKIP'
            'SKIP')

prepare() {
	cd "${_srcname}/"

	git submodule init
	git config submodule.lib/uxplay.url "${srcdir}/uxplay"
	git config submodule.lib/idevice-rs.url "${srcdir}/idevice"
	git -c protocol.file.allow=always submodule update

	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target host-tuple
}

build() {
	cd "${_srcname}/"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
	export CFLAGS+=" -ffat-lto-objects"
	export CXXFLAGS+=" -ffat-lto-objects"
	cargo build --release --features package_manager
}

package() {
	cd "${_srcname}/"
	local _app_id="io.github.${pkgname}.${_srcname}"

	install -Dm755 "target/release/${pkgname}" -t "${pkgdir}/usr/bin/"
	install -Dm644 "${_app_id}.desktop" -t "${pkgdir}/usr/share/applications/"
	install -Dm644 "${_app_id}.metainfo.xml" -t "${pkgdir}/usr/share/metainfo/"

	for r in 16 32 256 512; do
		install -Dm644 "packaging/shared/resources/app-icon/icon-${r}.png" \
			"${pkgdir}/usr/share/icons/hicolor/${r}x${r}/apps/${_app_id}.png"
	done
}
