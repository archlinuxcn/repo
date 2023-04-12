# Maintainer: sukanka<su975853527 AT gmail dot com>
pkgname=clash-verge
pkgver=1.3.1
pkgrel=2
pkgdesc="A Clash GUI based on tauri."
arch=('x86_64' 'aarch64')
url="https://github.com/zzzgydi/clash-verge"
license=('GPL3')
depends=('webkit2gtk' 'clash-geoip' 'libayatana-appindicator')
makedepends=('yarn' 'cargo-tauri' 'clash-premium-bin' 'clash-meta'  'jq' 'moreutils' 'rust' 'quickjs')
optdepends=('clash-premium-bin: clash-core'
'clash-meta: clash-core')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
"${pkgname}.desktop"
)

sha512sums=('8f44f7888617d1ae0d371da2c66d43dfc9dd79ec883b900d984f3a8a3c3385a4eb4ec31c2a48e016c05653bbd11d148f0b144c41a8e0841f3b90d5e08f909cf2'
            '2066dacf2e5e0135e6403cbfb825efcdf08bbcdc781407e6bb1fbb85143817b2b1abef641d20390ff7e5b3e91a509933e9eb17a64f9de7671445ac6d5363a44a')

prepare(){
	cd $srcdir/${pkgname}-${pkgver}

	install -d src-tauri/sidecar
	ln -sf /usr/bin/clash src-tauri/sidecar/clash-${CARCH}-unknown-linux-gnu
	ln -sf /usr/bin/clash-meta src-tauri/sidecar/clash-meta-${CARCH}-unknown-linux-gnu

	install -d src-tauri/resources
	ln -sf /etc/clash/Country.mmdb src-tauri/resources/Country.mmdb
	jq 'del(.scripts.prepare)' package.json|sponge package.json

	cd src-tauri
	# only build the excutable
	jq '.tauri.bundle.active = false' tauri.conf.json|sponge tauri.conf.json
	# disable updater
	jq '.tauri.updater.active = false' tauri.conf.json|sponge tauri.conf.json

}

build(){
	cd $srcdir/${pkgname}-${pkgver}
	# export HOME=$srcdir
	export RUSTFLAGS="-L /usr/lib/quickjs"
	yarn install
	yarn run check
	cargo-tauri build
}
package(){
	cd $srcdir/${pkgname}-${pkgver}
	install -Dm755 src-tauri/target/release/${pkgname} -t ${pkgdir}/usr/bin

	install -d ${pkgdir}/usr/lib/${pkgname}/resources
	ln -sf /etc/clash/Country.mmdb -t ${pkgdir}/usr/lib/${pkgname}/resources

	install -Dm644 src/assets/image/logo.svg ${pkgdir}/usr/share/icons/hicolor/scalable/apps/${pkgname}.svg

	install -Dm644 ${srcdir}/${pkgname}.desktop -t ${pkgdir}/usr/share/applications

}
