# Maintainer: Integral <integral@member.fsf.org>

pkgname=waylyrics
pkgver=0.3.21
pkgrel=3
pkgdesc="the furry way to show desktop lyrics"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/${pkgname}/${pkgname}"
license=("MIT")
depends=(
	"openssl" "dbus" "glibc" "libgcc" "glib2" "cairo" "dconf" "gtk4" "opencc"
)
makedepends=("cargo" "gettext")
optdepends=(
	"breeze-icons: better tray-icon icons"
	"xdg-desktop-portal: file dialog to import LRC"
)
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('7279ae1e6d25845d3baac08e8d515e7fa44881ad51146d08a25a3477e2388681')
options=('!lto')

_features=(--features opencc
           --features action-event
           --features offline-test)

prepare() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target host-tuple
}

build() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	export WAYLYRICS_THEME_PRESETS_DIR="/usr/share/${pkgname}/themes/"
	# --all-features introduced dbus/vendored feature, we prefer system dbus here.
	cargo build --release --frozen "${_features[@]}"
}

check() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	export WAYLYRICS_THEME_PRESETS_DIR="/usr/share/${pkgname}/themes/"
	cargo test --frozen "${_features[@]}"
}

package() {
	depends+=("hicolor-icon-theme")

	cd "${pkgname}-${pkgver}/"
	local _app_id=io.github.waylyrics.Waylyrics

	install -Dm755 "target/release/${pkgname}" -t "${pkgdir}/usr/bin/"
	install -Dm644 "metainfo/${_app_id}.desktop" -t "${pkgdir}/usr/share/applications/"
	install -Dm644 "metainfo/${_app_id}.gschema.xml" -t "${pkgdir}/usr/share/glib-2.0/schemas/"
	install -Dm644 "metainfo/${_app_id}.metainfo.xml" -t "${pkgdir}/usr/share/metainfo/"
	install -Dm644 themes/*.css -t "${pkgdir}/usr/share/${pkgname}/themes/"

	for locale in locales/*/LC_MESSAGES/waylyrics.po; do
		echo "Installing locale $locale..."
		mo=${locale/#locales\//} # */LC_MESSAGES/waylyrics.po
		mo=${mo/%.po/.mo}        # */LC_MESSAGES/waylyrics.mo
		msgfmt "${locale}" -o - | install -Dm644 /dev/stdin "${pkgdir}/usr/share/locale/${mo}"
	done

	install -Dm644 "res/icons/hicolor/scalable/apps/${_app_id}.svg" -t "${pkgdir}/usr/share/icons/hicolor/scalable/apps/"
	install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}
