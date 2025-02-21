# Maintainer: cubercsl <2014cais01 at gmail dot com>

pkgname=dae
pkgver=1.0.0rc2
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
sha256sums=('505ac11f1d1616c15b9c64427a7fd679011797e80ed4313cb0e4745edc5f5aa9')

build() {
	export CFLAGS="-fno-stack-protector"
	export CGO_ENABLED=1
	export CGO_CPPFLAGS="${CPPFLAGS}"
	export CGO_CFLAGS="${CFLAGS}"
	export CGO_CXXFLAGS="${CXXFLAGS}"
	export CGO_LDFLAGS="${LDFLAGS}"
	export BUILD_ARGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
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
