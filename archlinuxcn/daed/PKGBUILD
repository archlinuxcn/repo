# Maintainer: Integral <integral@member.fsf.org>
# Maintainer: cubercsl <2014cais01 at gmail dot com>

pkgname=daed
pkgver=0.18.0
pkgrel=1
pkgdesc="A modern dashboard for dae, bundled with dae-wing (backend API server) and dae (core)."
arch=('x86_64' 'aarch64')
url="https://github.com/daeuniverse/${pkgname}"
license=('AGPL-3.0-or-later AND MIT')
depends=('v2ray-geoip' 'v2ray-domain-list-community')
makedepends=('pnpm' 'clang' 'go')
provides=('dae')
conflicts=('dae')
source=("${pkgname}-${pkgver}.zip::${url}/releases/download/v${pkgver}/${pkgname}-full-src.zip")
sha512sums=('9cf3df0debf57b14075e554108aac0ea137a3cf7104fc59da39ef7b031548cca4d935f8086b351bfaadb7fac783f553dac8151313ea4d6c19b756e78131d95ba')
install="${pkgname}.install"
options=(!debug)

build() {
	export CFLAGS="-fno-stack-protector"
	export CGO_ENABLED=1
	export CGO_CPPFLAGS="${CPPFLAGS}"
	export CGO_CFLAGS="${CFLAGS}"
	export CGO_CXXFLAGS="${CXXFLAGS}"
	export CGO_LDFLAGS="${LDFLAGS}"
	export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
	make VERSION="${pkgver}"
}

package() {
	install -vDm755 "${pkgname}" -t "${pkgdir}/usr/bin/"
	install -vDm644 "install/${pkgname}.service" -t "${pkgdir}/usr/lib/systemd/system/"
	install -vDm644 "LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}/"
	install -d "${pkgdir}/usr/share/${pkgname}/"
	ln -vs "/usr/share/v2ray/geoip.dat" "${pkgdir}/usr/share/${pkgname}/geoip.dat"
	ln -vs "/usr/share/v2ray/geosite.dat" "${pkgdir}/usr/share/${pkgname}/geosite.dat"
}
