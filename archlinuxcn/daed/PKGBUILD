# Maintainer: Integral <integral@member.fsf.org>
# Maintainer: cubercsl <2014cais01 at gmail dot com>

pkgname=daed
pkgver=0.7.4
pkgrel=1
pkgdesc="A modern dashboard for dae, bundled with dae-wing (backend API server) and dae (core)."
arch=('x86_64' 'aarch64')
url="https://github.com/daeuniverse/${pkgname}"
license=('AGPL-3.0-or-later AND MIT')
makedepends=('pnpm' 'clang' 'go')
provides=('dae')
conflicts=('dae')
source=("${pkgname}-${pkgver}.zip::https://github.com/daeuniverse/${pkgname}/releases/download/v${pkgver}/${pkgname}-full-src.zip")
sha512sums=('d3b6823d5286f3f42a047d971f798ea1680ef55f1d1302919e22d1db8bc0383daa706831d80382a8413abd068175f4958a658fc835b97e4cf8aa40e70d9b1302')
install="${pkgname}.install"
options=(!debug)

build() {
	export GOFLAGS="-buildmode=pie -trimpath -modcacherw"
	export CFLAGS="-fno-stack-protector"
	sed -i 's/git rev-parse --short HEAD/echo/' vite.config.ts
	make VERSION="${pkgver}"
}

package() {
	depends=(
		v2ray-geoip
		v2ray-domain-list-community
	)

	install -vDm755 "${pkgname}" -t "${pkgdir}/usr/bin/"
	install -vDm644 "install/${pkgname}.service" -t "${pkgdir}/usr/lib/systemd/system/"
	install -vDm644 "LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}/"
	install -d "${pkgdir}/etc/daed/"

	install -d "${pkgdir}/usr/share/daed/"
	ln -vs "/usr/share/v2ray/geoip.dat" "${pkgdir}/usr/share/daed/geoip.dat"
	ln -vs "/usr/share/v2ray/geosite.dat" "${pkgdir}/usr/share/daed/geosite.dat"
}
