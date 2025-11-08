# Maintainer: Integral <integral@member.fsf.org>
# Contributor: Pylogmon <pylogmon@outlook.com>

pkgname=clash-verge-rev
_pkgname=${pkgname%-rev}
pkgver=2.4.3
pkgrel=1
pkgdesc="Continuation of Clash Verge | A Clash Meta GUI based on Tauri"
arch=('x86_64' 'i686' 'aarch64' 'armv7h')
url="https://github.com/${pkgname}/${pkgname}"
license=('GPL-3.0-or-later')
depends=('webkit2gtk-4.1' 'gtk3' 'libayatana-appindicator' 'mihomo')
conflicts=("${_pkgname}")
provides=("${_pkgname}")
makedepends=('pnpm' 'cargo' 'jq' 'moreutils')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
	"${_pkgname}-service.tar.gz::https://github.com/${pkgname}/${_pkgname}-service/archive/refs/tags/${CARCH}-unknown-linux-gnu.tar.gz")
sha512sums=('d2e93f59a003eb05fd0bdaa985298ecf7d9a403ad7e908dcd87c3bf19651f07b6c67b5305f4ec2d749eb6ec281eba1b2badde973e0d697343b8705523b5c6032'
            '9dbce77076b07691b5359b3e91c82190880f6caad291102fa28d8480bba53c27c8bac324032cbfee74e69653e2e97e54c430d17ad4fc5aaeb7a833d1b6598a4b')

prepare() {
	cd "${pkgname}-${pkgver}/"
	jq '.bundle.createUpdaterArtifacts = false' src-tauri/tauri.conf.json | sponge src-tauri/tauri.conf.json
	pnpm i
}

build() {
	cd "${_pkgname}-service-${CARCH}-unknown-linux-gnu/"
	export CFLAGS+=" -ffat-lto-objects"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	_prepare_service
	_build_service
	_check_service
	_package_service

	cd "../${pkgname}-${pkgver}/"
	install -d ./src-tauri/sidecar/

	# Use empty files as placeholders
	touch ./src-tauri/sidecar/verge-mihomo{,-alpha}-${CARCH}-unknown-linux-gnu

	install -vDm644 ./src/locales/* -t ./src-tauri/resources/locales/
	pnpm build -b deb
}

package() {
	cp -a ${pkgname}-${pkgver}/src-tauri/target/release/bundle/deb/Clash\ Verge_${pkgver}_*/data/* "${pkgdir}"
	ln -sf /usr/bin/mihomo "${pkgdir}/usr/bin/verge-mihomo"
	ln -sf /usr/bin/mihomo "${pkgdir}/usr/bin/verge-mihomo-alpha"
}

_prepare_service() {
	echo "==> Starting ${FUNCNAME[0]}()..."
	cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

_build_service() {
	echo "==> Starting ${FUNCNAME[0]}()..."
	cargo build --frozen --release --all-features
}

_check_service() {
	echo "==> Starting ${FUNCNAME[0]}()..."
	cargo test --frozen --all-features
}

_package_service() {
	echo "==> Starting ${FUNCNAME[0]}()..."

	for bin in {${_pkgname},{,un}install}-service; do
		install -vDm755 "./target/release/${bin}" "../${pkgname}-${pkgver}/src-tauri/resources/${bin}-${CARCH}-unknown-linux-gnu"
	done
}
