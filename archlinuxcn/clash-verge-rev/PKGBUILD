# Maintainer: Integral <integral@member.fsf.org>
# Contributor: Pylogmon <pylogmon@outlook.com>

pkgname=clash-verge-rev
_pkgname=${pkgname%-rev}
pkgver=2.5.8
_ipc_ver=2.7.6
pkgrel=1
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
sha512sums=('e381d642000641d9490fa53ec5adf346b263e48f7837f97fe8506091a307b24d36652317451847db263920a42944dc06aec8b34f31c505fc6bf970954e02b380'
            '238b7aa9f9a202bad37c57877400d9a2b87fd9f06eb591941ca260877c6e49be0a83de76cd0cf91ef27d37ff9b554698a1fea2b98681e89df14ef7dd26f7d8be'
            'ff3fac4e2b517c998d79c56c79d64be048cce44ffa67e5bb738bdfef2cea169843d2770a3a186e875df857b8da7d8472a701add1d87768889d48ff43b329defd'
            '2752df0baf8217c95fbb0d602b5254ad5e5c9fd122664ea80ca74a4c540ea1a647dbb5b94009b4922722484c32d2feae5cc42fbe35bd9a99ff324fefd67b3927'
            '397c6f7f0aac1c16a1c44e647345965049945bfd36e7d338f688968c9429d7d91d9a1c69afa29dc3310c6386f5b33e31bfbf9b83bcbf08638faac36dfa92bc4e')

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
