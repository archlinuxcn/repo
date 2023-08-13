# Maintainer: Integral <integral@murena.io>
# Maintainer: cubercsl <2014cais01 at gmail dot com>

pkgname=daed
pkgver=0.3.3
pkgrel=1
pkgdesc="A modern dashboard for dae, bundled with dae-wing (backend API server) and dae (core)."
arch=('x86_64' 'aarch64')
url="https://github.com/daeuniverse/daed"
license=('AGPL' 'MIT')
makedepends=('pnpm' 'clang' 'go')
provides=('daed')
conflicts=('daed')
source=("${pkgname}-${pkgver}.zip::https://github.com/daeuniverse/${pkgname}/releases/download/v${pkgver}/${pkgname}-full-src.zip")
sha512sums=('d53042cbe497e64dd37ea4a3abf381384a5fc4f483f8241d89ac456bd754907e96b901dc14d9ed4295d6dc0a7dbb339687cb4db20a1088f48bd2fcec5ef30d6e')
options=(!debug)

build() {
	export GOFLAGS="-buildmode=pie -trimpath -modcacherw"
	export CFLAGS="-fno-stack-protector"
	cd "${srcdir}"
	sed -i 's/git rev-parse --short HEAD/echo/' vite.config.ts
	make VERSION="${pkgver}"
}

package() {
	depends=(
		v2ray-geoip
		v2ray-domain-list-community
	)

	cd "${srcdir}"

	install -vDm755 "${pkgname}" -t "${pkgdir}/usr/bin/"
	install -vDm644 "install/${pkgname}.service" -t "${pkgdir}/usr/lib/systemd/system/"
	install -vDm644 "LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
	install -d "${pkgdir}/etc/daed/"

	mkdir -p "${pkgdir}/usr/share/daed"
	ln -vs "/usr/share/v2ray/geoip.dat" "${pkgdir}/usr/share/daed/geoip.dat"
	ln -vs "/usr/share/v2ray/geosite.dat" "${pkgdir}/usr/share/daed/geosite.dat"
}
