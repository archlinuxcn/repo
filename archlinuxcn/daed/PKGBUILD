# Maintainer: Integral <integral@murena.io>
# Maintainer: cubercsl <2014cais01 at gmail dot com>

pkgname=daed
pkgver=0.1.0rc
pkgrel=1
pkgdesc="A modern dashboard for dae, bundled with dae-wing (backend API server) and dae (core)."
arch=('x86_64')
url="https://github.com/daeuniverse/daed"
license=('AGPL' 'MIT')
makedepends=('git' 'pnpm' 'clang' 'go')
provides=('daed')
conflicts=('daed')
source=("git+https://github.com/daeuniverse/${pkgname}.git#branch=release-v${pkgver}")
sha256sums=('SKIP')
options=(!debug)

prepare() {
	cd "${srcdir}/${pkgname}"
	git submodule update --init --recursive
}

build() {
	export GOFLAGS="-buildmode=pie -trimpath -modcacherw"
	export CFLAGS="-fno-stack-protector"
	cd "${srcdir}/${pkgname}"
	make VERSION="unstable-${pkgver}"
}

package() {
	depends=(
		v2ray-geoip
		v2ray-domain-list-community
	)

	cd "${srcdir}/${pkgname}"

	install -vDm755 "${pkgname}" -t "${pkgdir}/usr/bin/"
	install -vDm644 "install/${pkgname}.service" -t "${pkgdir}/usr/lib/systemd/system/"
	install -vDm644 "LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
	install -d "${pkgdir}/etc/daed/"

	mkdir -p "${pkgdir}/usr/share/daed"
	ln -vs "/usr/share/v2ray/geoip.dat" "${pkgdir}/usr/share/daed/geoip.dat"
	ln -vs "/usr/share/v2ray/geosite.dat" "${pkgdir}/usr/share/daed/geosite.dat"

	echo "After installation completed, open your browser and navigate to http://localhost:2023"
}
