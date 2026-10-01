# Maintainer: Integral <integral@member.fsf.org>
# Contributor: Pylogmon <pylogmon@outlook.com>

pkgname=clash-verge-rev
_pkgname=${pkgname%-rev}
pkgver=2.5.6
_ipc_ver=2.7.4
pkgrel=4
pkgdesc="Continuation of Clash Verge | A Clash Meta GUI based on Tauri"
arch=('x86_64' 'i686' 'aarch64' 'armv7h')
url="https://github.com/${pkgname}/${pkgname}"
license=('GPL-3.0-or-later')
depends=('webkit2gtk-4.1' 'gtk3' 'libayatana-appindicator' 'mihomo' 'zstd')
conflicts=("${_pkgname}")
provides=("${_pkgname}")
makedepends=('pnpm' 'rust' 'jq' 'moreutils')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
	"${_pkgname}-service-ipc-${_ipc_ver}.tar.gz::https://github.com/${pkgname}/${_pkgname}-service-ipc/archive/v${_ipc_ver}.tar.gz"
	https://github.com/MetaCubeX/meta-rules-dat/releases/download/latest/{Country.mmdb,geo{ip,site}.dat}
)
sha512sums=('27288656661e2887f4eb0fc1e59e1ca288be95af79b8a73c729b8a96f897e06705d69a5b1711308a4c9008aaec1663fb32675f44798b3f0c94be72911ce4f7ce'
            '99af310d318694ab6818696e0426ccc9517a2191125668013aa2524a9922bf2134de7f762fa69fd95060206d3cb4574005dc5af579b0a7ff4c4f6b0bf3b315ff'
            'c8cc6032d20a4a1097873007ab68ebee114302cdb9b5b4bdb726e8938634d4140207cdb88f57a2db87137770620c01f889ddc472f47055f6b453117a4e7ab0c5'
            'a31ca8f7291022260be7295a213aee97dee7970b183694b0f57b923cfc2d562a54c6135a0421cae7ea2c116dcbbb6cffe62951ce0e94899519361a767cdc8228'
            '94c2030429642635ce11c05177cffdc48d81548d4f6c32b9666800b84fbb3a733838d3e0887bc91389aa9706f2402bfd8ea634327edafb5d9c6f8d3bcef7ee0d')

prepare() {
	pushd "${_pkgname}-service-ipc-${_ipc_ver}/"
	_prepare_service
	popd

	cd "${pkgname}-${pkgver}/"
	jq '.bundle.createUpdaterArtifacts = false' src-tauri/tauri.conf.json | sponge src-tauri/tauri.conf.json
	pnpm i

	cd src-tauri
	cargo fetch --locked --target host-tuple
}

build() {
	pushd "${_pkgname}-service-ipc-${_ipc_ver}/"
	export CFLAGS+=" -ffat-lto-objects"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
	export AWS_LC_SYS_NO_JITTER_ENTROPY=1
	export ZSTD_SYS_USE_PKG_CONFIG=1
	_build_service
	_package_service
	popd

	cd "${pkgname}-${pkgver}/"
	install -Dm644 ${srcdir}/{Country.mmdb,geo{ip,site}.dat} -t ./src-tauri/resources

	# Use empty files as placeholders
	touch ./src-tauri/sidecar/verge-mihomo{,-alpha}-${CARCH}-unknown-linux-gnu

	pnpm build -b deb
}

package() {
	cp -a ${pkgname}-${pkgver}/src-tauri/target/release/bundle/deb/Clash\ Verge_${pkgver}_*/data/* "${pkgdir}"
	ln -sf /usr/bin/mihomo "${pkgdir}/usr/bin/verge-mihomo"
	ln -sf /usr/bin/mihomo "${pkgdir}/usr/bin/verge-mihomo-alpha"
}

_prepare_service() {
	echo "==> Starting ${FUNCNAME[0]}()..."
	cargo fetch --locked --target host-tuple
}

_build_service() {
	echo "==> Starting ${FUNCNAME[0]}()..."
	cargo build --frozen --release --features "standalone client"
}

_package_service() {
	echo "==> Starting ${FUNCNAME[0]}()..."

	pushd target/release
	local _sidecar_dir="${srcdir}/${pkgname}-${pkgver}/src-tauri/sidecar"
	local _suffix="${CARCH}-unknown-linux-gnu"
	install -Dm755 "${_pkgname}-service" "${_sidecar_dir}/${_pkgname}-service-${_suffix}"
	install -Dm755 "${_pkgname}-service-install" "${_sidecar_dir}/${_pkgname}-service-install-${_suffix}"
	install -Dm755 "${_pkgname}-service-uninstall" "${_sidecar_dir}/${_pkgname}-service-uninstall-${_suffix}"
	popd
}
