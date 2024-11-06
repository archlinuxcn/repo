# Maintainer: cubercsl <2014cais01 at gmail dot com>

pkgname=dae
pkgver=0.9.0rc1
pkgrel=2
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
sha256sums=('f96455861e8dcdf5e05736a68ab900d1195f35a4836b32dfa1cd2eced0990155')

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
