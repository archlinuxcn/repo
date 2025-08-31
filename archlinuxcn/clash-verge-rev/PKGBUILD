# Maintainer: Integral <integral@member.fsf.org>
# Contributor: Pylogmon <pylogmon@outlook.com>

pkgname=clash-verge-rev
_pkgname=${pkgname%-rev}
pkgver=2.4.1
pkgrel=1
pkgdesc="Continuation of Clash Verge | A Clash Meta GUI based on Tauri"
arch=('x86_64' 'i686' 'aarch64' 'armv7h')
url="https://github.com/${pkgname}/${pkgname}"
license=('GPL-3.0-or-later')
depends=('webkit2gtk-4.1' 'gtk3' 'libayatana-appindicator' 'mihomo')
conflicts=("${_pkgname}")
provides=("${_pkgname}")
makedepends=('pnpm' 'cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
	"${_pkgname}-service.tar.gz::https://github.com/${pkgname}/${_pkgname}-service/archive/refs/tags/${CARCH}-unknown-linux-gnu.tar.gz")
sha512sums=('ff8dffd2d6600444fec890480735654896930fc07fb050250ef126382cc811f30dcea45d268b1e537cead97801c4466768ee270f662e9b3a2bdc938679a107e3'
            '13fc59c1e075de77f13b556457287c02f98a2e077640b5543da8543783df5f6b6c9c24e255b98b1c4d4009e68f53d5dbed4f863627267f8e4732ace2baec1811')

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
