# Maintainer: kiri@vern.cc
# Contributor: sukanka<su975853527 AT gmail dot com>

pkgname=clash-verge
pkgver=1.5.4
pkgrel=1
pkgdesc="A Clash Meta GUI based on Tauri, Continuation of Clash Verge"
arch=('x86_64' 'aarch64')
url="https://github.com/clash-verge-rev/clash-verge-rev"
license=('GPL-3.0-or-later')
depends=('cairo'
         'clash-geoip'
         'clash-meta'  
         'gcc-libs'
         'gdk-pixbuf2'
         'glib2'
         'glibc'
         'gtk3'
         'hicolor-icon-theme'
         'libayatana-appindicator'
         'libsoup'
         'openssl'
         'webkit2gtk')
makedepends=('cargo-tauri'
             'jq'
             'moreutils'
             'pnpm'
             'rust')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
	    "${pkgname}.desktop"
)
sha512sums=('e2e6fd79afe9c23a053f2081c08b22b47a6f816ceb999c5a0a60043058267ea049c8131962f7b320434162ec8661173bf52324a2bb8e76914f6e8c5d9cc46bd3'
            '2066dacf2e5e0135e6403cbfb825efcdf08bbcdc781407e6bb1fbb85143817b2b1abef641d20390ff7e5b3e91a509933e9eb17a64f9de7671445ac6d5363a44a')
options=(!lto)

prepare() {
	mv ${pkgname}-rev-${pkgver} ${pkgname}-${pkgver}
	cd $srcdir/${pkgname}-${pkgver}
	install -d src-tauri/sidecar
	install -d src-tauri/resources
	# empty files as placeholders
	touch src-tauri/sidecar/clash{,-meta-alpha,-meta}-${CARCH}-unknown-linux-gnu
	touch src-tauri/resources/Country.mmdb
	touch src-tauri/resources/geo{ip,site}.dat

	jq 'del(.scripts.prepare)' package.json | sponge package.json

	cd src-tauri
	# only build the excutable
	jq '.tauri.bundle.active = false' tauri.conf.json | sponge tauri.conf.json
}

build() {
	cd $srcdir/${pkgname}-${pkgver}
	# export HOME=$srcdir
	pnpm install
	pnpm run check
	cargo-tauri build
}

package() {
	cd $srcdir/${pkgname}-${pkgver}
	install -Dm755 src-tauri/target/release/${pkgname} -t ${pkgdir}/usr/bin

	install -d ${pkgdir}/usr/lib/${pkgname}/resources
	ln -sf /etc/clash/Country.mmdb -t ${pkgdir}/usr/lib/${pkgname}/resources

	install -Dm644 src/assets/image/logo.svg ${pkgdir}/usr/share/icons/hicolor/scalable/apps/${pkgname}.svg

	install -Dm644 ${srcdir}/${pkgname}.desktop -t ${pkgdir}/usr/share/applications
}
