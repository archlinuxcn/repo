# Maintainer: Integral <integral@member.fsf.org>
# Contributor: Pylogmon <pylogmon@outlook.com>

pkgname=clash-verge-rev
_pkgname=${pkgname%-rev}
pkgver=2.5.4
_ipc_ver=2.7.2
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
sha512sums=('0aee41a15120009875fedc07c7cd3e0d28ffb72f871dff94662696857e4923084309779aa5dcc9bf79a662305ca1d22bcfd33c09b438a66be898be59ff124e2b'
            '436affca4969822d3ba234a22bbcc14574d930d7acce7728995c4ebef1189ec076e4e9a07fa55398ab2932d8df2998e585bca5a2da5f00e43692d441655161b9'
            'a5402e5d295f56dd5a09783dca99b689c8ea1744436d1fdddb78291d25c769c85c40950c5fa8476747bf8afbe9c758ff0f27d8e15b93883631226993877f9a4a'
            '995a7c62b1afdfb1c3541c749ff04375428ebfdee1f05d569ee742cc6dc5a5de30daf640411e1599d57ef64736bd8a8fda1d1e9c2b7c099fa499c27c013ced30'
            '0740e3558432db745817d67e288e3d0f385c154a644e5f62a7f3c9ddccf523faece5fb04ddf027f1dc038383f25a176bf20959c541507f7b5b851a9fe43ce249')

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
