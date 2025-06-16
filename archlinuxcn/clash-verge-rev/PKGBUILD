# Maintainer: Integral <integral@member.fsf.org>
# Contributor: Pylogmon <pylogmon@outlook.com>

pkgname=clash-verge-rev
_pkgname=${pkgname%-rev}
pkgver=2.3.0
pkgrel=1
pkgdesc="Continuation of Clash Verge | A Clash Meta GUI based on Tauri"
arch=('x86_64' 'i686' 'aarch64' 'armv7h')
url="https://github.com/${pkgname}/${pkgname}"
license=('GPL-3.0-or-later')
depends=('webkit2gtk-4.1' 'gtk3' 'libayatana-appindicator' 'clash-meta')
conflicts=("${_pkgname}")
provides=("${_pkgname}")
makedepends=('pnpm' 'cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
	"${_pkgname}-service.tar.gz::https://github.com/${pkgname}/${_pkgname}-service/archive/refs/tags/${CARCH}-unknown-linux-gnu.tar.gz")
sha512sums=('da6f0fa24f70b4abba14e92534896cce9910395eae842134f8cc7f43b3b069b302398155e580221e91b25008c5bac713629c5756705f7510acff6a9992dc20dd'
            '53973fd6a38e4268898bc6eb7665fba0f8fdcdf6d57917e1fd873304157512c2845a803a1c6825cd97390bdb01fe37fa0e30f292e3116c0d29e579d508cfa84b')
install="${pkgname}.install"

prepare() {
	cd "${pkgname}-${pkgver}/"
	sed -i '/createUpdaterArtifacts/s/true/false/' src-tauri/tauri.conf.json
	pnpm i
}

build() {
	cd "${_pkgname}-service-${CARCH}-unknown-linux-gnu/"
	export CFLAGS+=" -ffat-lto-objects"
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
	ln -sf /usr/bin/clash-meta "${pkgdir}/usr/bin/verge-mihomo"
	ln -sf /usr/bin/clash-meta "${pkgdir}/usr/bin/verge-mihomo-alpha"
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
