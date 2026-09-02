# Maintainer: Integral <integral@member.fsf.org>

pkgname=waylyrics
pkgver=0.4.2
pkgrel=2
pkgdesc="the furry way to show desktop lyrics"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/${pkgname}/${pkgname}"
license=("MIT")
depends=(
	"openssl" "dbus" "glibc" "libgcc" "glib2" "cairo" "dconf" "gtk4"
)
makedepends=("git" "cargo" "gettext")
optdepends=(
	"breeze-icons: better tray-icon icons"
	"xdg-desktop-portal: file dialog to import LRC"
)
source=("git+${url}#tag=v${pkgver}")
sha256sums=('722363cb2169b598e6f2af3ba1b610124f0488a97552d63ece322fa17e7acfbc')
options=('!lto')

_features=(--features action-event
           --features offline-test)

prepare() {
	cd "${pkgname}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --target host-tuple
}

build() {
	cd "${pkgname}/"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	export WAYLYRICS_THEME_PRESETS_DIR="/usr/share/${pkgname}/themes/"
	# --all-features introduced dbus/vendored feature, we prefer system dbus here.
	cargo build --release --frozen "${_features[@]}"
}

check() {
	cd "${pkgname}/"
	export RUSTUP_TOOLCHAIN=stable
	export WAYLYRICS_THEME_PRESETS_DIR="/usr/share/${pkgname}/themes/"
	cargo test --frozen "${_features[@]}"
}

package() {
	depends+=("hicolor-icon-theme")

	cd "${pkgname}/"
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
		install -Dm644 <(msgfmt "${locale}" -o -) "${pkgdir}/usr/share/locale/${mo}"
	done

	install -Dm644 "res/icons/hicolor/scalable/apps/${_app_id}.svg" -t "${pkgdir}/usr/share/icons/hicolor/scalable/apps/"
	install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}
