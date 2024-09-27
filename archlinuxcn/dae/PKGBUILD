# Maintainer: cubercsl <2014cais01 at gmail dot com>

pkgname=dae
pkgver=0.8.0rc2
pkgrel=1
pkgdesc="A Linux lightweight and high-performance transparent proxy solution based on eBPF."
arch=('x86_64' 'aarch64')
url="https://github.com/daeuniverse/${pkgname}"
license=('AGPL-3.0-or-later')
depends=(
	'glibc'
	'v2ray-geoip'
	'v2ray-domain-list-community'
)
makedepends=('clang' 'go')
backup=("etc/${pkgname}/config.${pkgname}")
source=("${pkgname}-${pkgver}.zip::${url}/releases/download/v${pkgver}/${pkgname}-full-src.zip")
install="${pkgname}.install"
sha256sums=('007e712bb1c21199dc748e052e0e175a4a16a576e7327d18c7a4d79c2e32722f')

build() {
	export GOFLAGS="-buildmode=pie -trimpath -modcacherw"
	export CFLAGS="-fno-stack-protector"
	make VERSION="${pkgver}"
}

package() {
	install -Dm755 "${pkgname}" -t "${pkgdir}/usr/bin/"
	install -Dm644 "install/${pkgname}.service" -t "${pkgdir}/usr/lib/systemd/system/"
	install -Dm640 "install/empty.${pkgname}" "${pkgdir}/etc/${pkgname}/config.${pkgname}"
	install -Dm644 "example.${pkgname}" "${pkgdir}/etc/${pkgname}/config.${pkgname}.example"

	mkdir -p "${pkgdir}/usr/share/${pkgname}/"
	ln -vs /usr/share/v2ray/geoip.dat "${pkgdir}/usr/share/${pkgname}/geoip.dat"
	ln -vs /usr/share/v2ray/geosite.dat "${pkgdir}/usr/share/${pkgname}/geosite.dat"
}
