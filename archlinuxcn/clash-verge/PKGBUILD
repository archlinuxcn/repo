# Maintainer: sukanka<su975853527 AT gmail dot com>
pkgname=clash-verge
pkgver=1.3.0
pkgrel=2
pkgdesc="A Clash GUI based on tauri."
arch=('x86_64' 'aarch64')
url="https://github.com/zzzgydi/clash-verge"
license=('GPL3')
depends=('webkit2gtk' 'clash-geoip' 'libayatana-appindicator')
makedepends=('yarn' 'cargo-tauri' 'clash-premium-bin' 'clash-meta'  'jq' 'moreutils' 'rust' 'quickjs')
optdepends=('clash-premium-bin>=2022.04.01: clash-core'
'clash-meta: clash-core')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
"${pkgname}.desktop"
"001-appimage.patch::https://github.com/zzzgydi/clash-verge/commit/2b6acedae1fa29646e10cee4483105fa3479a2d6.patch"
"002-grant-permission-for-linux.patch::https://github.com/zzzgydi/clash-verge/commit/52658886e75cd2f06fb125fcb74da5a3452275e5.patch"
)

sha512sums=('2bcbbc242056bbc889e29c0afb2b2b409838f6ee4ffdec3da976f44ff687659f2a15e71b5a65d41d59e18666fc3fda7ebe7478cbd91abb37d9beebb80570b8e0'
            '2066dacf2e5e0135e6403cbfb825efcdf08bbcdc781407e6bb1fbb85143817b2b1abef641d20390ff7e5b3e91a509933e9eb17a64f9de7671445ac6d5363a44a'
            '9a81ba8de8410fda1c7f892bc2dfb0dec8214ea6f86a605bb5ea36f4f55fa1092697a96d4de6c649e1b90c332ed67275255690d25b0f2a711fbf6f2cd4c3729e'
            'fb946048c578e4258595599fe85093c1f768683f6fa46e353c4ca93e882b086216243f353d49b4346265cc53f57ed6cdabfeea73245611f0992a63b5e3426375')

prepare(){
	cd $srcdir/${pkgname}-${pkgver}
	patch -p1 < $srcdir/001-*.patch
	patch -p1 < $srcdir/002-*.patch

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
