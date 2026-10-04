# Maintainer: Integral <integral@member.fsf.org>
# Contributor: Pylogmon <pylogmon@outlook.com>

pkgname=clash-verge-rev
_pkgname=${pkgname%-rev}
pkgver=2.5.7
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
sha512sums=('60bd8eb0e4d8d3b6c7355c943abfab50ce0c1ce3a3c95ccaccc576216ae4c08db7bba34d1006cc687bec5f646f9b97f2530ed3a3c9623d2bb17a978454250230'
            '238b7aa9f9a202bad37c57877400d9a2b87fd9f06eb591941ca260877c6e49be0a83de76cd0cf91ef27d37ff9b554698a1fea2b98681e89df14ef7dd26f7d8be'
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
