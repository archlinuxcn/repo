# Maintainer: kiri@vern.cc
# Contributor: sukanka<su975853527 AT gmail dot com>

pkgname=clash-verge
pkgver=1.7.7
pkgrel=1
pkgdesc="A Clash Meta GUI based on Tauri, Continuation of Clash Verge"
arch=('x86_64' 'aarch64')
url="https://github.com/clash-verge-rev/clash-verge-rev"
license=('GPL-3.0-or-later')
depends=('cairo'
         'clash-geoip' # provide: Country.mmdb
	 'meta-rules-dat' # provide: geoip.dat and geosite.dat
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
makedepends=('jq'
             'moreutils'
             'pnpm'
             'rust')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
	    "${pkgname}.desktop"
)
sha512sums=('22d915d2946ad327236769aa95594060dfd8f0e53d3e6d7c6a567512a2152ac80797afa45104a0b7f200abe37bba7629567fa4d0d247324c154e009fe76231d4'
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
	pnpm run web:build
	cd src-tauri
	cargo build --release
}

package() {
	cd $srcdir/${pkgname}-${pkgver}
	install -Dm755 src-tauri/target/release/${pkgname} -t ${pkgdir}/usr/bin

	install -d ${pkgdir}/usr/lib/${pkgname}/resources
	ln -sf /etc/clash/Country.mmdb -t ${pkgdir}/usr/lib/${pkgname}/resources
        ln -sf /etc/clash/geoip.dat -t ${pkgdir}/usr/lib/${pkgname}/resources
	ln -sf /etc/clash/geosite.dat -t ${pkgdir}/usr/lib/${pkgname}/resources
 
        ln -sf /usr/bin/clash-meta  ${pkgdir}/usr/bin/verge-mihomo
 	install -Dm755 src-tauri/target/release/resources/{clash-verge,install,uninstall}-service -t ${pkgdir}/usr/lib/${pkgname}/resources

	install -Dm644 src-tauri/icons/icon.png ${pkgdir}/usr/share/icons/hicolor/512x512/apps/${pkgname}.png

	install -Dm644 ${srcdir}/${pkgname}.desktop -t ${pkgdir}/usr/share/applications
}
