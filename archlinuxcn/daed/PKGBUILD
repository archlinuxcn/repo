# Maintainer: Integral <integral@member.fsf.org>
# Maintainer: cubercsl <2014cais01 at gmail dot com>

pkgname=daed
pkgver=1.22.0
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
sha512sums=('b79cfcce8561ad5fc41a0d8cc404f7f57b0e343a3b388bed24e6b474f3186119421531bd5371c4c56151e254862d09ce50eb0ca86f50ffe486bf01571ebf5822')
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
