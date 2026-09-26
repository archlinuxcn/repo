# Maintainer: Integral <integral@member.fsf.org>
# Contributor: Pylogmon <pylogmon@outlook.com>

pkgname=clash-verge-rev
_pkgname=${pkgname%-rev}
pkgver=2.5.6
_ipc_ver=2.7.4
pkgrel=2
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
            '76ee007cb219cc410019b911a3122f9350f8541a1dccddca25b556b73ecd81f4cdc12dacdf130bd2f7897382d12dd6fb143b326c4ca800959d05ebc9f797fdcd'
            'a95613562a1f586f8edc3ca695bc1329ec91a8c85ea70a0045808ba60ab6d17cf1f80c91e45e1f7da02cdbfdce9d36d1b6ede971f84957765bca36badc8d367b'
            '9f24c55471cd2e36929fcb223c5e3f434d74b4ed4e2150bd95f5d51b607457c8387a33ed691b4580a4f2c987c13eedffeb4f78fbdb5d8ecf0139e60fada98ef7')

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
